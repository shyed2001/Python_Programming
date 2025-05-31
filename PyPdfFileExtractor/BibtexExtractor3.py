# import time
# import requests
# import re
# import sys
# import logging
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# # ================================
# # CONFIGURATION
# # ================================
# MAX_RETRIES = 7
# BASE_DELAY = 7  # Seconds between retries
# LOG_FILE = 'bibtex_extractor.log'
# OUTPUT_FILE = 'BibTeX_output.bib'
# UNFINISHED_FILE = 'unfinished_urls.txt'

# # Initialize logging
# logging.basicConfig(
#     filename=LOG_FILE,
#     level=logging.INFO,
#     format='%(asctime)s - %(levelname)s - %(message)s',
#     filemode='w'
# )

# def get_chrome_options():
#     """Configure Chrome options to suppress warnings and improve stability"""
#     options = Options()
#     options.add_argument("--headless")
#     options.add_argument("--disable-gpu")
#     options.add_argument("--no-sandbox")
#     options.add_argument("--disable-dev-shm-usage")
#     options.add_argument("--log-level=3")
#     options.add_experimental_option('excludeSwitches', ['enable-logging'])
#     options.add_argument("--disable-blink-features=AutomationControlled")
#     return options

# # ================================
# # URL PROCESSING
# # ================================
# def extract_urls(text):
#     """Extract arXiv and Semantic Scholar URLs with validation"""
#     patterns = {
#         'arxiv': r'https://arxiv.org/abs/(\d+\.\d+)',
#         'semanticscholar': r'https://www.semanticscholar.org/paper/(?:[^/]+/)?([a-f0-9]+)'
#     }
    
#     return {
#         'arxiv': list(set(re.findall(patterns['arxiv'], text))),
#         'semanticscholar': list(set(re.findall(patterns['semanticscholar'], text)))
#     }

# # ================================
# # BIBTEX FETCHERS
# # ================================
# def fetch_arxiv_bibtex(paper_id):
#     """Retrieve BibTeX from arXiv API with error handling"""
#     try:
#         url = f'https://arxiv.org/bibtex/{paper_id}'
#         response = requests.get(url, timeout=15)
#         response.raise_for_status()
#         return response.text.strip()
#     except Exception as e:
#         logging.error(f"arXiv {paper_id}: {str(e)}")
#         return None

# def fetch_semanticscholar_api(paper_id):
#     """Fetch metadata from Semantic Scholar API with rate limit handling"""
#     try:
#         url = f'https://api.semanticscholar.org/graph/v1/paper/{paper_id}?fields=title,authors,year,venue,externalIds,url'
#         response = requests.get(url, timeout=15)
        
#         if response.status_code == 429:
#             raise RuntimeError("API rate limit exceeded")
            
#         response.raise_for_status()
#         data = response.json()
        
#         authors = " and ".join([a['name'] for a in data.get('authors', [])])
#         return (
#             f"@article{{{paper_id},\n"
#             f"  title = {{{data.get('title', '')}}},\n"
#             f"  author = {{{authors}}},\n"
#             f"  journal = {{{data.get('venue', '')}}},\n"
#             f"  year = {{{data.get('year', '')}}},\n"
#             f"  doi = {{{data.get('externalIds', {}).get('DOI', '')}}},\n"
#             f"  url = {{{data.get('url', '')}}}\n}}"
#         )
#     except Exception as e:
#         logging.warning(f"SS API {paper_id}: {str(e)}")
#         return None

# def fetch_semanticscholar_selenium(paper_id):
#     """Fallback method using browser automation with enhanced stability"""
#     driver = webdriver.Chrome(options=get_chrome_options())
#     try:
#         driver.get(f"https://www.semanticscholar.org/paper/{paper_id}")
        
#         # Wait for core page elements
#         WebDriverWait(driver, 25).until(
#             EC.presence_of_element_located((By.CSS_SELECTOR, 'main#paper-details'))
#         )
        
#         # Retry click logic with page refresh
#         for _ in range(3):
#             try:
#                 WebDriverWait(driver, 15).until(
#                     EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-heap-nav="citing-paper"]'))
#                 ).click()
#                 break
#             except:
#                 driver.refresh()
#                 time.sleep(3)

#         WebDriverWait(driver, 15).until(
#             EC.element_to_be_clickable((By.XPATH, '//button[contains(., "BibTeX")]'))
#         ).click()
        
#         return WebDriverWait(driver, 15).until(
#             EC.visibility_of_element_located((By.CSS_SELECTOR, "pre"))
#         ).text.strip()
        
#     except Exception as e:
#         logging.error(f"Selenium {paper_id}: {str(e)}")
#         return None
#     finally:
#         driver.quit()

# # ================================
# # PROCESSING CORE
# # ================================
# def process_urls(urls, fetch_func, context):
#     """Process URLs with enhanced rate limit handling and interrupt support"""
#     results = []
#     unfinished = []
    
#     try:
#         for idx, paper_id in enumerate(urls, 1):
#             result = None
#             for attempt in range(MAX_RETRIES + 1):
#                 try:
#                     result = fetch_func(paper_id)
#                     if result: 
#                         break
                    
#                     # Exponential backoff with base delay
#                     delay = BASE_DELAY * (2 ** attempt)
#                     logging.info(f"Retry {attempt+1}/{MAX_RETRIES} for {paper_id} in {delay}s")
#                     time.sleep(delay)
                    
#                 except KeyboardInterrupt:
#                     logging.info("User interrupted processing")
#                     raise
#                 except Exception as e:
#                     logging.warning(f"Attempt {attempt+1} failed: {str(e)}")
#                     time.sleep(BASE_DELAY * (attempt + 1))
            
#             if result:
#                 results.append(result)
#                 # Strategic throttling
#                 if idx % 3 == 0:
#                     time.sleep(3)
#                 if idx % 10 == 0:
#                     logging.info(f"Progress: {idx}/{len(urls)}")
#                     time.sleep(7)
#             else:
#                 unfinished.append(paper_id)
#                 logging.error(f"Failed {paper_id} after {MAX_RETRIES} retries")
                
#     except KeyboardInterrupt:
#         logging.info("Saving partial results before exit")
#         save_results(results)
#         save_unfinished(unfinished + urls[idx:])
#         sys.exit(0)
        
#     return results, unfinished

# # ================================
# # UTILITIES
# # ================================
# def save_results(entries):
#     """Save collected entries to output file"""
#     try:
#         with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
#             f.write("\n\n".join(entries))
#         logging.info(f"Saved {len(entries)} entries to {OUTPUT_FILE}")
#     except Exception as e:
#         logging.error(f"Failed to save results: {str(e)}")

# def save_unfinished(urls):
#     """Save unfinished URLs for later processing"""
#     try:
#         with open(UNFINISHED_FILE, 'w') as f:
#             f.write("\n".join(urls))
#         logging.info(f"Saved {len(urls)} unfinished URLs")
#     except Exception as e:
#         logging.error(f"Failed to save unfinished list: {str(e)}")

# # ================================
# # MAIN EXECUTION FLOW
# # ================================
# def main():
#     # Extract and validate URLs from input file
#     with open('URL_input.txt') as f:
#         urls = extract_urls(f.read())
    
#     # Process arXiv URLs
#     arxiv_results, arxiv_unfinished = process_urls(
#         urls['arxiv'], 
#         fetch_arxiv_bibtex,
#         {'start_time': time.time()}
#     )
    
#     # Process Semantic Scholar URLs
#     ss_results, ss_unfinished = process_urls(
#         urls['semanticscholar'],
#         lambda pid: fetch_semanticscholar_api(pid) or fetch_semanticscholar_selenium(pid),
#         {'start_time': time.time()}
#     )
    
#     # Save final results
#     save_results(arxiv_results + ss_results)
#     save_unfinished(arxiv_unfinished + ss_unfinished)

# if __name__ == "__main__":
#     try:
#         main()
#     except Exception as e:
#         logging.critical(f"Critical error: {str(e)}")
#         sys.exit(1)



import time
import requests
import re  # For regular expressions
import sys  # For system exit on error
from selenium import webdriver  # For Selenium scraping
from selenium.webdriver.chrome.options import Options  # For setting up the Selenium browser
from selenium.webdriver.common.by import By  # For locating elements in Selenium

# ================================
# STEP 1: Input Raw Text with URLs
# ================================
# This is where we input the raw text that contains the URLs.
raw_text = """
# Your list of URLs here (for example)

[1] https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/58780524/8e72b0cd-c569-4b3d-a24b-cf5bceae98ad/paste.txt
[2] https://www.semanticscholar.org/paper/df04c41baa151e38bc49a2dde2e6eab1c8fd638d
[3] https://www.semanticscholar.org/paper/1ac0755e8443dd7f6a8734531b65bacb580f054d
[4] https://www.semanticscholar.org/paper/f39f4630d860f4b49e08ed609ce40fcbaac29582
[5] https://www.semanticscholar.org/paper/57aa6550ea5165d79aa7ef891404bbe5b20c51be
[6] https://www.semanticscholar.org/paper/7fb086ee40031be973c8ab8c4e05547181f14534
[7] https://www.semanticscholar.org/paper/5723ce91ee691c64a9348295e0e124640cd158fb
[8] https://www.semanticscholar.org/paper/42d951f482efa55c3e0586d56d5a75361c7b3cee
[9] https://www.semanticscholar.org/paper/353e1ff915bb4db0c242a633518480120b14a6e4
[11] https://www.cambridge.org/core/journals/knowledge-engineering-review/article/blockchainbased-database-management-system/9F946ACEB1041D6B075F593ABE024BDF
[12] https://www.semanticscholar.org/paper/941d21e783fb6b7d46ff54b3d2a34cd3f428c86c
[13] https://www.scylladb.com/glossary/blockchain-database/
[14] https://www.reddit.com/r/datascience/comments/f38ks9/where_do_you_see_databases_going_in_the_future/
[15] https://www.techtarget.com/searchcio/tip/Blockchain-vs-database-Similarities-differences-explained
[16] https://www.reddit.com/r/AskProgramming/comments/1f07skq/why_is_the_mern_stack_ridiculed/
[17] https://www.reddit.com/r/devops/comments/1ez9zpt/whats_the_point_of_nosql/
[18] https://arxiv.org/pdf/2111.00416.pdf
[19] https://research.monash.edu/files/360365412/343562757_oa.pdf
[20] https://stlpartners.com/articles/edge-computing/whats-blockchain-got-to-do-with-edge-computing/
[21] https://www.sciencedirect.com/science/article/pii/S1084804524000614
[22] https://www.semanticscholar.org/paper/8f1160f145a135cf512948649bd70ad35a70fe8e
[23] https://arxiv.org/abs/2305.07453
[24] https://www.semanticscholar.org/paper/c842eba7e795e52301b25f00f50b6ed550d1775a
[25] https://www.semanticscholar.org/paper/06365a5d675173464b72a277ff2881c97f5443a7
[26] https://www.reddit.com/r/IAmA/comments/14prsnz/i_produced_a_matteroffact_documentary_film_that/
[27] https://www.reddit.com/r/ethdev/comments/wpj198/blockchain_developer_as_a_1st_job/
[28] https://www.reddit.com/r/programming/comments/xglxew/explore_the_new_era_of_databases_the_surrealdb/
[29] https://www.reddit.com/r/askscience/comments/6tut5w/how_does_a_computer_network_like_hbos_handle_the/
[30] https://www.reddit.com/r/webdev/comments/r9xnxs/is_web3_really_the_future/
[31] https://www.reddit.com/r/OMSCS/comments/qnutd3/who_are_taking_cs6675/
[32] https://www.reddit.com/r/programming/comments/15mgp4i/spacetimedb_a_new_database_written_in_rust_that/
[33] https://lumendatabase.org/notices/40528529
[34] https://www.sciencedirect.com/science/article/abs/pii/S0140366423002566
[35] https://www.mdpi.com/2079-9292/10/9/1000
[36] https://www.semanticscholar.org/paper/6714780b2b0315c7f76017318ab3f2f4ec55071a
[37] https://www.semanticscholar.org/paper/fea80ba0cccabbbe64956b32c5bfdd5ef73c0580
[38] https://www.semanticscholar.org/paper/1bd6c38338bbb44b6ab4ca6af36a0a20b5e1f06d
[39] https://www.semanticscholar.org/paper/c6eb2370c71ab98588aeb12a2a0c71cb31c55785
[40] https://www.reddit.com/r/databasedevelopment/comments/unj8d1/getting_started_with_database_development/
[41] https://www.reddit.com/r/learnprogramming/comments/12kckyj/has_anyone_studied_the_open_source_society/?tl=bn
[42] https://www.reddit.com/r/csMajors/comments/1dxu7wt/confused_about_choosing_specialization_in_bsc/
[43] https://www.reddit.com/r/developersPak/comments/1iyo9vw/advice_stand_out_in_the_market/
[44] https://www.reddit.com/r/learnprogramming/comments/7vvpw9/trying_to_learn_web_development_looking_for_a/
[45] https://www.reddit.com/r/Btechtards/comments/zy0p2n/cse_domains/
[46] https://www.reddit.com/r/CryptoReality/wiki/talkingpoints/
[47] https://www.sciencedirect.com/science/article/pii/S1319157819309000
[48] https://www.sciencedirect.com/science/article/abs/pii/B9780323918503000019
[49] https://www.semanticscholar.org/paper/3c590beb7dcd6c3a083de8cc97d7ebb3c523eca4
[50] https://www.semanticscholar.org/paper/469df80e88204a613c6013d48d482d073739b5eb
[51] https://www.reddit.com/r/Bitcoin/comments/4j7wjf/bigchaindb_a_prime_example_of_blockchain_bullshit/
[52] https://www.reddit.com/r/OMSCS/comments/1g9ka4o/feedback_on_a_new_omscs_course_on_building/
[53] https://builtin.com/software-engineering-perspectives/grid-computing
[54] https://coincentral.com/grid-computing-the-powers-of-distributed-cloud-computing/
[55] https://www.spiceworks.com/tech/cloud/articles/what-is-grid-computing/
[1] https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/58780524/8e72b0cd-c569-4b3d-a24b-cf5bceae98ad/paste.txt
[2] https://www.semanticscholar.org/paper/389dac07e147c04278de2bc6d1f890a515d16cdc
[3] https://www.reddit.com/r/CryptoTechnology/comments/te1lwc/whats_the_closest_a_blockchain_can_get_from_being/
[4] https://www.reddit.com/r/singularity/comments/1dmap17/possible_timelines_for_gpt45_and_gpt5/
[5] https://www.reddit.com/r/ComputerEngineering/comments/1cozdlb/parallelcommittees_a_novelle_secure_and/
[6] https://www.reddit.com/r/ObsidianMD/comments/1gl8w1i/on_the_value_of_graph_view/
[7] https://www.comp.nus.edu.sg/~ooibc/hybriddb-vldb22.pdf
[8] https://www.semanticscholar.org/paper/04808c682ed5c839132c6bd4202dcfadf258568a
[9] https://onlinelibrary.wiley.com/doi/10.1002/itl2.604
[10] https://www.timestored.com/data/time-series-database-benchmarks
[11] https://academic.oup.com/database/article/doi/10.1093/database/baab026/6277712
[12] https://www.vldb.org/pvldb/vol15/p1092-loghin.pdf
[13] https://www.semanticscholar.org/paper/ad72ee630ab32f293e6273ee20d22724355bfe45
[14] https://www.neuroquantology.com/open-access/HYBRID+BLOCKCHAIN+DATABASE+SYSTEMS+DESIGN+AND+PERFORMANCE_14194/
[15] https://www.semanticscholar.org/paper/adb58f1b47ac90559157da0aa5f10b6ef6c80e25
[16] http://sites.computer.org/debull/A22june/p48.pdf
[17] https://www.semanticscholar.org/paper/23e2ca6f0fa725c973320227e8a04e925ba50a06
[18] https://www.semanticscholar.org/paper/4b7270f34f1d956ad2a3506d7a2d5fe52bcd4746
[19] https://www.reddit.com/r/dotnet/comments/1h5zc80/multiple_databases_in_clean_architecture_good/
[20] https://www.reddit.com/r/vectordatabase/comments/1gi4bxp/vector_db_usecases/
[21] https://200oksolutions.com/blog/modern-database-architectures-hybrid-approach-sql-nosql-newsql-2025/
[22] https://www.semanticscholar.org/paper/3494df53b4a491464a6d265a268d0904d4968de6
[23] https://www.semanticscholar.org/paper/c267b8f9d633e46e51f036df271d3fcd16c32086
[24] https://www.semanticscholar.org/paper/b317ba6505141d605032c4dcee9579e1bb599206
[25] https://www.semanticscholar.org/paper/7f4953b7e252a7e5677cfde959cad6b52b42c54e
[26] https://www.reddit.com/r/CryptoTechnology/comments/7wal16/binances_woes_are_why_distributed_database/
[27] https://www.reddit.com/r/singularity/comments/1dz9laf/one_of_openais_next_supercomputing_clusters_will/
[28] https://www.reddit.com/r/OMSCS/comments/1g9ka4o/feedback_on_a_new_omscs_course_on_building/
[29] https://www.reddit.com/r/ExperiencedDevs/comments/phzek0/why_no_one_uses_graph_databases/
[30] https://www.reddit.com/r/dataengineering/comments/1hmef51/your_upcoming_2025_de_projects/
[31] https://www.reddit.com/r/programming/comments/jegq9k/blockchain_the_amazing_solution_for_almost_nothing/
[32] https://www.reddit.com/r/Futurology/comments/1h4dzer/how_would_supercomputers_look_like_and_operate_in/
[33] https://www.reddit.com/r/softwarearchitecture/comments/1jadsjp/input_on_architecture_for_distributed_document/
[34] https://www.reddit.com/r/MachineLearning/comments/1eg674y/discussion_thoughts_on_knowledge_graphs_and_graph/
[35] https://www.reddit.com/r/softwarearchitecture/comments/1fhn858/monolith_vs_microservices_or_hybrid_approach/
[36] https://www.reddit.com/r/dotnet/comments/cdhwho/when_should_a_nosql_solution_be_used_ever/
[37] https://www.reddit.com/r/singularity/comments/163zck4/google_to_spend_25_billion_building_one_zettaflop/
[38] https://www.reddit.com/r/java/comments/18u344k/whats_the_point_of_in_memory_databases_are_they/
[39] https://www.reddit.com/r/learnmachinelearning/comments/1h1yt2j/using_an_inmemory_graph_database_for_graphrag_in/
[40] https://bitcoinke.io/2022/03/why-use-nosql-together-with-blockchain-technology/
[41] https://questdb.com
[42] https://ignite.apache.org/use-cases/in-memory-database.html
[43] http://musingsaboutlibrarianship.blogspot.com/2020/09/graph-based-applications-for-academic.html
[44] https://www.dataversity.net/hybrid-database-architectures-lead-the-way/
[45] https://arxiv.org/abs/2305.03592
[46] https://www.datacamp.com/blog/time-series-database
[47] https://kestra.io/blogs/embedded-databases
[48] https://dl.acm.org/doi/10.1145/3626203.3670539
[49] https://pandorafms.com/blog/database-types-and-best-ones/
[50] https://sci-hub.se/downloads/2020-05-25/45/10.1109@ICCCBDA49378.2020.9095589.pdf
[51] https://www.opennms.com/time-series-db/
[52] https://www.ipdps.org/ipdps2025/2025-call-for-papers.html
[53] https://www.sciencedirect.com/science/article/pii/S0926580525000743
[54] https://www.semanticscholar.org/paper/6c91030f6833bafe765c906858033e8a3efb8ede
[55] https://www.semanticscholar.org/paper/d422a46e205bf57307af24b95727d7d5c943a669
[56] https://www.semanticscholar.org/paper/2dffe684c13d33b2582f611d8960c2bb0aa4b204
[57] https://www.semanticscholar.org/paper/86aaa954793c24103a6e1c036b2714aac30d27ea
[58] https://www.reddit.com/r/Bitcoin/comments/316sdy/to_ibm_stop_this_blockchain_nonsense_it_will/
[59] https://www.reddit.com/r/dataengineering/comments/1iny0wj/what_are_your_hobby_programming_languagesprojects/
[60] https://www.reddit.com/user/Inery_blockchain/
[61] https://www.reddit.com/r/developersIndia/comments/18pn3kt/what_are_you_planning_to_learn_in_2024/
[62] https://www.reddit.com/r/CryptoCurrency/comments/wo62th/the_people_who_hate_on_blockchain_usecases/
[63] https://www.reddit.com/r/ExperiencedDevs/comments/1iys1e8/how_do_you_come_up_with_side_projects_that/
[64] https://lumendatabase.org/notices/40528529
[65] https://dl.acm.org/doi/10.14778/3510397.3510406
[66] https://www.sciencedirect.com/science/article/abs/pii/S1389128623001317
[67] https://research.ibm.com/publications/blockchains-and-databases-a-new-era-in-distributed-computing
[68] https://hazelcast.com/foundations/data-and-middleware-technologies/in-memory-data-grid/
[69] https://www.softwaretestinghelp.com/hybrid-database/
[70] https://www.semanticscholar.org/paper/1d4c87a85879cf25d1e0251049de334cea3fcd3c
[71] https://www.semanticscholar.org/paper/4f58e308fbdc28f9f07136fb683c2fd7448e4549
[72] https://www.semanticscholar.org/paper/2ce85d3fea771e56081dd6594eaa9dd008229564
[73] https://www.semanticscholar.org/paper/3b205c4b790176e0e4080ea20e987c40de52db40
[74] https://www.semanticscholar.org/paper/6cd8ab1fb564ee4b006d12876f950fc834d6fd0e
[75] https://www.semanticscholar.org/paper/31862a3ae03d8b1f4a28d0dce712dee8c3af87de
[76] https://www.reddit.com/r/Bitcoin/comments/uxmmfw/why_are_utxo_commitments_not_a_thing/
[77] https://www.reddit.com/r/devops/comments/1ez9zpt/whats_the_point_of_nosql/
[78] https://www.reddit.com/r/Futurology/comments/oed4o4/i_am_the_senior_research_scientist_at_agi/
[79] https://www.reddit.com/r/dataengineering/comments/yl1r8m/what_actually_is_master_data_management_and_what/
[1] https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/58780524/a9a80488-fec7-46a0-b6db-02d8ad1e9cad/paste.txt
[2] https://pubmed.ncbi.nlm.nih.gov/18383062/
[3] https://www.semanticscholar.org/paper/c654e1700571d1979166b0e7f70969efb9aba50b
[4] https://www.semanticscholar.org/paper/a33bedabe271e2227488c6a1ab29df4242e26c05
[5] https://www.semanticscholar.org/paper/95e7c44a42ab97bfedc0d68753d773843ea83f93
[6] https://www.semanticscholar.org/paper/71d4cb79741c81cc814da4e1a8a245ec08012ca8
[7] https://www.semanticscholar.org/paper/86f63bf54a17ea4ab7e95f5ca732c6b6372350e2
[8] https://www.semanticscholar.org/paper/40d8d6243149844fb8987fe7faa5300c2e51b083
[9] https://pubmed.ncbi.nlm.nih.gov/40069496/
[10] https://www.semanticscholar.org/paper/0147d174e2b30cbfa4f0555e34f7f352e4e04c37
[11] https://www.semanticscholar.org/paper/bf60ee864b92c8fc36bf177c00233cdfd55fdd24
[12] https://www.semanticscholar.org/paper/7d58916b2b3f4abee8a6c1b5a36d020a287ad1cc
[13] https://www.semanticscholar.org/paper/d05b0d3b195b7c168cff37653df659ec717c3b23
[1] https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/58780524/a9a80488-fec7-46a0-b6db-02d8ad1e9cad/paste.txt
[2] https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/58780524/63617646-2504-40d0-ad17-0c29f0f5f13a/paste-2.txt
[3] https://www.semanticscholar.org/paper/23354e6c4a6fa2e01c24064edca4c79f98288b1f
[4] https://www.semanticscholar.org/paper/435463d1eb51558d6b17fe508f56858ea2b4a64d
[5] https://www.semanticscholar.org/paper/20be3d6a456eeda3c23b3108fc2d49906d115306
[6] https://www.semanticscholar.org/paper/52b04a4b11acec2109edf2d99aa7765a9ea50848
[7] https://www.semanticscholar.org/paper/84937378e7bfe6f994b4db901658e725ac7003f1
[8] https://www.semanticscholar.org/paper/3fb0b2a7b48b1c34ff1bc4df4e749134faf7de17
[9] https://www.semanticscholar.org/paper/776132ecb3f30240b16bd7d4a3e8774496dd5fc3
[10] https://www.semanticscholar.org/paper/2a3647d14f5b5073f65d002ea63c41a025e20527
[11] https://www.semanticscholar.org/paper/16043995e1af25f5c0022b91350131b1302e0d4c
[12] https://www.semanticscholar.org/paper/7d44533aa513c79bb8ea3c36c93c0229bbcbf218
[13] https://www.semanticscholar.org/paper/a10b0c9a120f5802b7983376d75d8f18cf456ecc
[14] https://www.semanticscholar.org/paper/74a6494d05cb17f2c8fc9a2e2bd6239949a17a2c
[15] https://www.semanticscholar.org/paper/b6008a8c4e40b086c47291443c74a9343aad7a88
[16] https://www.semanticscholar.org/paper/5ac7280fcc308e35e9e693b10cec73fc68cc9996
[17] https://www.semanticscholar.org/paper/7bae73d34481614f554dca375a8aa6c27c431caf
[18] https://www.semanticscholar.org/paper/e46ad3875beebc1d2f070c959ad42ecb9ee565a8
[19] https://www.semanticscholar.org/paper/2b6f8f3f782937509ab58fdd18d6a6d66e55710e
[20] https://www.semanticscholar.org/paper/73f972f488b154f3788364de76adfb9ff25ee436
[21] https://www.semanticscholar.org/paper/76908d923308e74fabdc704dd42571e10488c0e6
[22] https://www.semanticscholar.org/paper/4aea2eb267f33562b32a47bc9c876bae600ad25c
[23] https://www.semanticscholar.org/paper/6ebba7a321a9159fc3b2f6dc8fd0777f7440fb01
[24] https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4284979/
[25] https://www.semanticscholar.org/paper/42152603b2546dc922485c1b1a0cb71378ddc309
[26] https://www.semanticscholar.org/paper/01d31210f538f330b9c1e98ce83afa1bc19325b1
[27] https://www.semanticscholar.org/paper/4f9f505caac311c1e5fd4d138adba4c88c69ce50
[28] https://www.semanticscholar.org/paper/6b8a84a0732cf30960044523562a2da2fde53f23





"""

# ================================
# STEP 2: Extract Specific URLs
# ================================
# Define regular expressions to match arXiv and Semantic Scholar URLs.
arxiv_pattern = r'https://arxiv.org/abs/\d+\.\d+'
# semanticscholar_pattern = r'https://www.semanticscholar.org/paper/[^/]+/\w+'
semanticscholar_pattern = r'https://www\.semanticscholar\.org/paper/(?:[^/]+/)?[\w-]+'
# Extract URLs using the defined patterns.
arxiv_urls = re.findall(arxiv_pattern, raw_text)
semanticscholar_urls = re.findall(semanticscholar_pattern, raw_text)

# ================================
# STEP 3: Define Fetch Functions for BibTeX
# ================================
def fetch_arxiv_bibtex(url):
    """
    Converts arXiv URL to its BibTeX representation by calling the bibtex endpoint.
    """
    try:
        bib_url = url.replace('/abs/', '/bibtex/')  # Change the URL to BibTeX endpoint
        response = requests.get(bib_url)
        if response.status_code == 200:
            bibtex = response.text.strip()
            # Ensure the BibTeX entry ends with a closing brace
            if not bibtex.endswith('}'):
                bibtex += '}'
            return bibtex
        else:
            return f"% Failed to fetch BibTeX from {url} (Status code: {response.status_code})"
    except Exception as e:
        return f"% Error fetching arXiv BibTeX for {url}: {str(e)}"

def fetch_semanticscholar_bibtex(url):
    """
    Extracts metadata from Semantic Scholar API and formats it as BibTeX.
    """
    try:
        paper_id = url.split("/")[-1]  # Extract the paper ID from the URL
        api_url = f"https://api.semanticscholar.org/graph/v1/paper/{paper_id}?fields=title,authors,year,venue,externalIds,url"
        response = requests.get(api_url)

        if response.status_code == 200:
            data = response.json()
            authors = " and ".join([author["name"] for author in data.get("authors", [])])
            title = data.get("title", "Unknown Title")
            journal = data.get("venue", "Unknown Journal")
            year = data.get("year", "n.d.")
            doi = data.get("externalIds", {}).get("DOI", None)

            # Prepare BibTeX entry with DOI, URL, and open access file link
            bibtex = (
                f"@article{{{paper_id},\n"
                f"  title={{ {title} }},\n"
                f"  author={{ {authors} }},\n"
                f"  journal={{ {journal} }},\n"
                f"  year={{ {year} }},\n"
                f"  doi={{ {doi} }},\n"
                f"  url={{ {data['url']} }}\n"
                f"}}"
            )
            return bibtex
        else:
            return f"% Failed to fetch from Semantic Scholar {url} (Status: {response.status_code})"
    except Exception as e:
        return f"% Error fetching Semantic Scholar BibTeX for {url}: {str(e)}"

# Function to fetch BibTeX from Semantic Scholar using Selenium (for fallback)
def fetch_semanticscholar_bibtex_selenium(url):
    """
    Scrapes BibTeX citation from Semantic Scholar using Selenium headless browser.
    Used when API fails or browser-only data is needed.
    """
    options = Options()
    options.add_argument("--headless")  # Run in headless mode (no GUI)
    driver = webdriver.Chrome(options=options)  # Initialize Selenium driver
    driver.get(url)  # Navigate to the Semantic Scholar paper page

    time.sleep(3)  # Wait for the page to load completely

    try:
        # Click citation button
        cite_button = driver.find_element(By.CSS_SELECTOR, 'button[data-heap-nav="citing-paper"]')
        cite_button.click()
        time.sleep(3)  # Wait for citation menu to open

        # Switch to BibTeX tab
        bibtex_tab = driver.find_element(By.XPATH, '//button[contains(text(), "BibTeX")]')
        bibtex_tab.click()
        time.sleep(3)  # Wait for BibTeX to load

        # Extract BibTeX text
        bibtex_text = driver.find_element(By.CSS_SELECTOR, "pre").text
    except Exception as e:
        print(f"Error with Selenium: {e}")
        bibtex_text = None
    finally:
        driver.quit()  # Close the Selenium browser

    # Return as parsed BibTeX entry if found
    if bibtex_text:
        return bibtex_text.strip()
    return None

# ================================
# STEP 4: Collect and Process Entries with Retry Logic
# ================================
# List to store all the BibTeX entries
bib_entries = []

# Function to implement the retry logic in case of 429 status
def fetch_with_retry(url, fetch_func, retry_count=1):
    """
    Fetches the BibTeX data and retries with a delay if 429 error is encountered.
    Implements exponential backoff to increase delay after each retry.
    """
    try:
        response = fetch_func(url)  # Call the fetch function
        # Retry if the status code is 429 (Too Many Requests)
        if '429' in response:
            print(f"Rate limit exceeded for {url}. Retrying after {7 * retry_count} seconds...")
            time.sleep(7 * retry_count)  # Exponential backoff (increase the sleep time)
            return fetch_with_retry(url, fetch_func, retry_count + 1)  # Retry the request with increased wait time
        return response
    except Exception as e:
        print(f"Error with URL {url}: {str(e)}")
        return None

# Process arXiv links
for index, url in enumerate(arxiv_urls):
    print(f"Fetching arXiv BibTeX for: {url}")
    bib = fetch_with_retry(url, fetch_arxiv_bibtex)
    if bib:
        bib_entries.append(bib)
    # Every 7 entries, pause for 17 seconds
    if (index + 1) % 7 == 0:
        print("Pausing for 7 seconds after processing 7 entries...")
        time.sleep(17)

# Process Semantic Scholar links
for index, url in enumerate(semanticscholar_urls):
    print(f"Fetching Semantic Scholar BibTeX for: {url}")
    bib = fetch_with_retry(url, fetch_semanticscholar_bibtex)
    if not bib:
        # If API call fails, fall back to Selenium method
        bib = fetch_with_retry(url, fetch_semanticscholar_bibtex_selenium)
    if bib:
        bib_entries.append(bib)
    
    
    # Every entries, pause for 5 seconds
    if (index + 1) % 1 == 0:
        print("Pausing for 5 seconds after processing each entries...")
        time.sleep(5)    
    # Every 3 entries, pause for 15 seconds
    if (index + 1) % 3 == 0:
        print("Pausing for 15 seconds after processing 3 entries...")
        time.sleep(15)
    # Every 7 entries, pause for 25 seconds
    if (index + 1) % 7 == 0:
        print("Pausing for 25 seconds after processing 7 entries...")
        time.sleep(25)

# ================================
# STEP 5: Save Output to .bib File
# ================================
output_file = "BibTeX_output_with_doi_url3.bib"
try:
    with open(output_file, "w", encoding="utf-8") as f:
        for entry in bib_entries:
            f.write(entry + "\n\n")
    print(f"✅ BibTeX entries saved to '{output_file}'")
except Exception as e:
    print(f"❌ Error writing to file: {e}")
    sys.exit(1)







# import time
# import requests
# import re  # For regular expressions
# import sys  # For system exit on error
# from selenium import webdriver  # For Selenium scraping
# from selenium.webdriver.chrome.options import Options  # For setting up the Selenium browser
# from selenium.webdriver.common.by import By  # For locating elements in Selenium
# import logging  # For logging script activity

# # ================================
# # STEP 1: Input Raw Text with URLs
# # ================================
# # This is where we input the raw text that contains the URLs.
# raw_text = """
# # Your list of URLs here (for example)


# [1] https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/58780524/8e72b0cd-c569-4b3d-a24b-cf5bceae98ad/paste.txt
# [2] https://www.semanticscholar.org/paper/df04c41baa151e38bc49a2dde2e6eab1c8fd638d
# [3] https://www.semanticscholar.org/paper/1ac0755e8443dd7f6a8734531b65bacb580f054d
# [4] https://www.semanticscholar.org/paper/f39f4630d860f4b49e08ed609ce40fcbaac29582
# [5] https://www.semanticscholar.org/paper/57aa6550ea5165d79aa7ef891404bbe5b20c51be
# [6] https://www.semanticscholar.org/paper/7fb086ee40031be973c8ab8c4e05547181f14534
# [7] https://www.semanticscholar.org/paper/5723ce91ee691c64a9348295e0e124640cd158fb
# [8] https://www.semanticscholar.org/paper/42d951f482efa55c3e0586d56d5a75361c7b3cee
# [9] https://www.semanticscholar.org/paper/353e1ff915bb4db0c242a633518480120b14a6e4
# [10] https://www.semanticscholar.org/paper/12b29ba78d91ad8a1ab463130d4316a5429fac5f
# [11] https://www.cambridge.org/core/journals/knowledge-engineering-review/article/blockchainbased-database-management-system/9F946ACEB1041D6B075F593ABE024BDF
# [12] https://www.semanticscholar.org/paper/941d21e783fb6b7d46ff54b3d2a34cd3f428c86c
# [13] https://www.scylladb.com/glossary/blockchain-database/
# [14] https://www.reddit.com/r/datascience/comments/f38ks9/where_do_you_see_databases_going_in_the_future/
# [15] https://www.techtarget.com/searchcio/tip/Blockchain-vs-database-Similarities-differences-explained
# [16] https://www.reddit.com/r/AskProgramming/comments/1f07skq/why_is_the_mern_stack_ridiculed/
# [17] https://www.reddit.com/r/devops/comments/1ez9zpt/whats_the_point_of_nosql/
# [18] https://arxiv.org/pdf/2111.00416.pdf
# [19] https://research.monash.edu/files/360365412/343562757_oa.pdf
# [20] https://stlpartners.com/articles/edge-computing/whats-blockchain-got-to-do-with-edge-computing/
# [21] https://www.sciencedirect.com/science/article/pii/S1084804524000614
# [22] https://www.semanticscholar.org/paper/8f1160f145a135cf512948649bd70ad35a70fe8e
# [23] https://arxiv.org/abs/2305.07453
# [24] https://www.semanticscholar.org/paper/c842eba7e795e52301b25f00f50b6ed550d1775a
# [25] https://www.semanticscholar.org/paper/06365a5d675173464b72a277ff2881c97f5443a7
# [26] https://www.reddit.com/r/IAmA/comments/14prsnz/i_produced_a_matteroffact_documentary_film_that/
# [27] https://www.reddit.com/r/ethdev/comments/wpj198/blockchain_developer_as_a_1st_job/
# [28] https://www.reddit.com/r/programming/comments/xglxew/explore_the_new_era_of_databases_the_surrealdb/
# [29] https://www.reddit.com/r/askscience/comments/6tut5w/how_does_a_computer_network_like_hbos_handle_the/
# [30] https://www.reddit.com/r/webdev/comments/r9xnxs/is_web3_really_the_future/
# [31] https://www.reddit.com/r/OMSCS/comments/qnutd3/who_are_taking_cs6675/
# [32] https://www.reddit.com/r/programming/comments/15mgp4i/spacetimedb_a_new_database_written_in_rust_that/
# [33] https://lumendatabase.org/notices/40528529
# [34] https://www.sciencedirect.com/science/article/abs/pii/S0140366423002566
# [35] https://www.mdpi.com/2079-9292/10/9/1000
# [36] https://www.semanticscholar.org/paper/6714780b2b0315c7f76017318ab3f2f4ec55071a
# [37] https://www.semanticscholar.org/paper/fea80ba0cccabbbe64956b32c5bfdd5ef73c0580
# [38] https://www.semanticscholar.org/paper/1bd6c38338bbb44b6ab4ca6af36a0a20b5e1f06d
# [39] https://www.semanticscholar.org/paper/c6eb2370c71ab98588aeb12a2a0c71cb31c55785
# [40] https://www.reddit.com/r/databasedevelopment/comments/unj8d1/getting_started_with_database_development/
# [41] https://www.reddit.com/r/learnprogramming/comments/12kckyj/has_anyone_studied_the_open_source_society/?tl=bn
# [42] https://www.reddit.com/r/csMajors/comments/1dxu7wt/confused_about_choosing_specialization_in_bsc/
# [43] https://www.reddit.com/r/developersPak/comments/1iyo9vw/advice_stand_out_in_the_market/
# [44] https://www.reddit.com/r/learnprogramming/comments/7vvpw9/trying_to_learn_web_development_looking_for_a/
# [45] https://www.reddit.com/r/Btechtards/comments/zy0p2n/cse_domains/
# [46] https://www.reddit.com/r/CryptoReality/wiki/talkingpoints/
# [47] https://www.sciencedirect.com/science/article/pii/S1319157819309000
# [48] https://www.sciencedirect.com/science/article/abs/pii/B9780323918503000019
# [49] https://www.semanticscholar.org/paper/3c590beb7dcd6c3a083de8cc97d7ebb3c523eca4
# [50] https://www.semanticscholar.org/paper/469df80e88204a613c6013d48d482d073739b5eb
# [51] https://www.reddit.com/r/Bitcoin/comments/4j7wjf/bigchaindb_a_prime_example_of_blockchain_bullshit/
# [52] https://www.reddit.com/r/OMSCS/comments/1g9ka4o/feedback_on_a_new_omscs_course_on_building/
# [53] https://builtin.com/software-engineering-perspectives/grid-computing
# [54] https://coincentral.com/grid-computing-the-powers-of-distributed-cloud-computing/
# [55] https://www.spiceworks.com/tech/cloud/articles/what-is-grid-computing/
# [1] https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/58780524/8e72b0cd-c569-4b3d-a24b-cf5bceae98ad/paste.txt
# [2] https://www.semanticscholar.org/paper/389dac07e147c04278de2bc6d1f890a515d16cdc
# [3] https://www.reddit.com/r/CryptoTechnology/comments/te1lwc/whats_the_closest_a_blockchain_can_get_from_being/
# [4] https://www.reddit.com/r/singularity/comments/1dmap17/possible_timelines_for_gpt45_and_gpt5/
# [5] https://www.reddit.com/r/ComputerEngineering/comments/1cozdlb/parallelcommittees_a_novelle_secure_and/
# [6] https://www.reddit.com/r/ObsidianMD/comments/1gl8w1i/on_the_value_of_graph_view/
# [7] https://www.comp.nus.edu.sg/~ooibc/hybriddb-vldb22.pdf
# [8] https://www.semanticscholar.org/paper/04808c682ed5c839132c6bd4202dcfadf258568a
# [9] https://onlinelibrary.wiley.com/doi/10.1002/itl2.604
# [10] https://www.timestored.com/data/time-series-database-benchmarks
# [11] https://academic.oup.com/database/article/doi/10.1093/database/baab026/6277712
# [12] https://www.vldb.org/pvldb/vol15/p1092-loghin.pdf
# [13] https://www.semanticscholar.org/paper/ad72ee630ab32f293e6273ee20d22724355bfe45
# [14] https://www.neuroquantology.com/open-access/HYBRID+BLOCKCHAIN+DATABASE+SYSTEMS+DESIGN+AND+PERFORMANCE_14194/
# [15] https://www.semanticscholar.org/paper/adb58f1b47ac90559157da0aa5f10b6ef6c80e25
# [16] http://sites.computer.org/debull/A22june/p48.pdf
# [17] https://www.semanticscholar.org/paper/23e2ca6f0fa725c973320227e8a04e925ba50a06
# [18] https://www.semanticscholar.org/paper/4b7270f34f1d956ad2a3506d7a2d5fe52bcd4746
# [19] https://www.reddit.com/r/dotnet/comments/1h5zc80/multiple_databases_in_clean_architecture_good/
# [20] https://www.reddit.com/r/vectordatabase/comments/1gi4bxp/vector_db_usecases/
# [21] https://200oksolutions.com/blog/modern-database-architectures-hybrid-approach-sql-nosql-newsql-2025/
# [22] https://www.semanticscholar.org/paper/3494df53b4a491464a6d265a268d0904d4968de6
# [23] https://www.semanticscholar.org/paper/c267b8f9d633e46e51f036df271d3fcd16c32086
# [24] https://www.semanticscholar.org/paper/b317ba6505141d605032c4dcee9579e1bb599206
# [25] https://www.semanticscholar.org/paper/7f4953b7e252a7e5677cfde959cad6b52b42c54e
# [26] https://www.reddit.com/r/CryptoTechnology/comments/7wal16/binances_woes_are_why_distributed_database/
# [27] https://www.reddit.com/r/singularity/comments/1dz9laf/one_of_openais_next_supercomputing_clusters_will/
# [28] https://www.reddit.com/r/OMSCS/comments/1g9ka4o/feedback_on_a_new_omscs_course_on_building/
# [29] https://www.reddit.com/r/ExperiencedDevs/comments/phzek0/why_no_one_uses_graph_databases/
# [30] https://www.reddit.com/r/dataengineering/comments/1hmef51/your_upcoming_2025_de_projects/
# [31] https://www.reddit.com/r/programming/comments/jegq9k/blockchain_the_amazing_solution_for_almost_nothing/
# [32] https://www.reddit.com/r/Futurology/comments/1h4dzer/how_would_supercomputers_look_like_and_operate_in/
# [33] https://www.reddit.com/r/softwarearchitecture/comments/1jadsjp/input_on_architecture_for_distributed_document/
# [34] https://www.reddit.com/r/MachineLearning/comments/1eg674y/discussion_thoughts_on_knowledge_graphs_and_graph/
# [35] https://www.reddit.com/r/softwarearchitecture/comments/1fhn858/monolith_vs_microservices_or_hybrid_approach/
# [36] https://www.reddit.com/r/dotnet/comments/cdhwho/when_should_a_nosql_solution_be_used_ever/
# [37] https://www.reddit.com/r/singularity/comments/163zck4/google_to_spend_25_billion_building_one_zettaflop/
# [38] https://www.reddit.com/r/java/comments/18u344k/whats_the_point_of_in_memory_databases_are_they/
# [39] https://www.reddit.com/r/learnmachinelearning/comments/1h1yt2j/using_an_inmemory_graph_database_for_graphrag_in/
# [40] https://bitcoinke.io/2022/03/why-use-nosql-together-with-blockchain-technology/
# [41] https://questdb.com
# [42] https://ignite.apache.org/use-cases/in-memory-database.html
# [43] http://musingsaboutlibrarianship.blogspot.com/2020/09/graph-based-applications-for-academic.html
# [44] https://www.dataversity.net/hybrid-database-architectures-lead-the-way/
# [45] https://arxiv.org/abs/2305.03592
# [46] https://www.datacamp.com/blog/time-series-database
# [47] https://kestra.io/blogs/embedded-databases
# [48] https://dl.acm.org/doi/10.1145/3626203.3670539
# [49] https://pandorafms.com/blog/database-types-and-best-ones/
# [50] https://sci-hub.se/downloads/2020-05-25/45/10.1109@ICCCBDA49378.2020.9095589.pdf
# [51] https://www.opennms.com/time-series-db/
# [52] https://www.ipdps.org/ipdps2025/2025-call-for-papers.html
# [53] https://www.sciencedirect.com/science/article/pii/S0926580525000743
# [54] https://www.semanticscholar.org/paper/6c91030f6833bafe765c906858033e8a3efb8ede
# [55] https://www.semanticscholar.org/paper/d422a46e205bf57307af24b95727d7d5c943a669
# [56] https://www.semanticscholar.org/paper/2dffe684c13d33b2582f611d8960c2bb0aa4b204
# [57] https://www.semanticscholar.org/paper/86aaa954793c24103a6e1c036b2714aac30d27ea
# [58] https://www.reddit.com/r/Bitcoin/comments/316sdy/to_ibm_stop_this_blockchain_nonsense_it_will/
# [59] https://www.reddit.com/r/dataengineering/comments/1iny0wj/what_are_your_hobby_programming_languagesprojects/
# [60] https://www.reddit.com/user/Inery_blockchain/
# [61] https://www.reddit.com/r/developersIndia/comments/18pn3kt/what_are_you_planning_to_learn_in_2024/
# [62] https://www.reddit.com/r/CryptoCurrency/comments/wo62th/the_people_who_hate_on_blockchain_usecases/
# [63] https://www.reddit.com/r/ExperiencedDevs/comments/1iys1e8/how_do_you_come_up_with_side_projects_that/
# [64] https://lumendatabase.org/notices/40528529
# [65] https://dl.acm.org/doi/10.14778/3510397.3510406
# [66] https://www.sciencedirect.com/science/article/abs/pii/S1389128623001317
# [67] https://research.ibm.com/publications/blockchains-and-databases-a-new-era-in-distributed-computing
# [68] https://hazelcast.com/foundations/data-and-middleware-technologies/in-memory-data-grid/
# [69] https://www.softwaretestinghelp.com/hybrid-database/
# [70] https://www.semanticscholar.org/paper/1d4c87a85879cf25d1e0251049de334cea3fcd3c
# [71] https://www.semanticscholar.org/paper/4f58e308fbdc28f9f07136fb683c2fd7448e4549
# [72] https://www.semanticscholar.org/paper/2ce85d3fea771e56081dd6594eaa9dd008229564
# [73] https://www.semanticscholar.org/paper/3b205c4b790176e0e4080ea20e987c40de52db40
# [74] https://www.semanticscholar.org/paper/6cd8ab1fb564ee4b006d12876f950fc834d6fd0e
# [75] https://www.semanticscholar.org/paper/31862a3ae03d8b1f4a28d0dce712dee8c3af87de
# [76] https://www.reddit.com/r/Bitcoin/comments/uxmmfw/why_are_utxo_commitments_not_a_thing/
# [77] https://www.reddit.com/r/devops/comments/1ez9zpt/whats_the_point_of_nosql/
# [78] https://www.reddit.com/r/Futurology/comments/oed4o4/i_am_the_senior_research_scientist_at_agi/
# [79] https://www.reddit.com/r/dataengineering/comments/yl1r8m/what_actually_is_master_data_management_and_what/
# [1] https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/58780524/a9a80488-fec7-46a0-b6db-02d8ad1e9cad/paste.txt
# [2] https://pubmed.ncbi.nlm.nih.gov/18383062/
# [3] https://www.semanticscholar.org/paper/c654e1700571d1979166b0e7f70969efb9aba50b
# [4] https://www.semanticscholar.org/paper/a33bedabe271e2227488c6a1ab29df4242e26c05
# [5] https://www.semanticscholar.org/paper/95e7c44a42ab97bfedc0d68753d773843ea83f93
# [6] https://www.semanticscholar.org/paper/71d4cb79741c81cc814da4e1a8a245ec08012ca8
# [7] https://www.semanticscholar.org/paper/86f63bf54a17ea4ab7e95f5ca732c6b6372350e2
# [8] https://www.semanticscholar.org/paper/40d8d6243149844fb8987fe7faa5300c2e51b083
# [9] https://pubmed.ncbi.nlm.nih.gov/40069496/
# [10] https://www.semanticscholar.org/paper/0147d174e2b30cbfa4f0555e34f7f352e4e04c37
# [11] https://www.semanticscholar.org/paper/bf60ee864b92c8fc36bf177c00233cdfd55fdd24
# [12] https://www.semanticscholar.org/paper/7d58916b2b3f4abee8a6c1b5a36d020a287ad1cc
# [13] https://www.semanticscholar.org/paper/d05b0d3b195b7c168cff37653df659ec717c3b23
# [1] https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/58780524/a9a80488-fec7-46a0-b6db-02d8ad1e9cad/paste.txt
# [2] https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/58780524/63617646-2504-40d0-ad17-0c29f0f5f13a/paste-2.txt
# [3] https://www.semanticscholar.org/paper/23354e6c4a6fa2e01c24064edca4c79f98288b1f
# [4] https://www.semanticscholar.org/paper/435463d1eb51558d6b17fe508f56858ea2b4a64d
# [5] https://www.semanticscholar.org/paper/20be3d6a456eeda3c23b3108fc2d49906d115306
# [6] https://www.semanticscholar.org/paper/52b04a4b11acec2109edf2d99aa7765a9ea50848
# [7] https://www.semanticscholar.org/paper/84937378e7bfe6f994b4db901658e725ac7003f1
# [8] https://www.semanticscholar.org/paper/3fb0b2a7b48b1c34ff1bc4df4e749134faf7de17
# [9] https://www.semanticscholar.org/paper/776132ecb3f30240b16bd7d4a3e8774496dd5fc3
# [10] https://www.semanticscholar.org/paper/2a3647d14f5b5073f65d002ea63c41a025e20527
# [11] https://www.semanticscholar.org/paper/16043995e1af25f5c0022b91350131b1302e0d4c
# [12] https://www.semanticscholar.org/paper/7d44533aa513c79bb8ea3c36c93c0229bbcbf218
# [13] https://www.semanticscholar.org/paper/a10b0c9a120f5802b7983376d75d8f18cf456ecc
# [14] https://www.semanticscholar.org/paper/74a6494d05cb17f2c8fc9a2e2bd6239949a17a2c
# [15] https://www.semanticscholar.org/paper/b6008a8c4e40b086c47291443c74a9343aad7a88
# [16] https://www.semanticscholar.org/paper/5ac7280fcc308e35e9e693b10cec73fc68cc9996
# [17] https://www.semanticscholar.org/paper/7bae73d34481614f554dca375a8aa6c27c431caf
# [18] https://www.semanticscholar.org/paper/e46ad3875beebc1d2f070c959ad42ecb9ee565a8
# [19] https://www.semanticscholar.org/paper/2b6f8f3f782937509ab58fdd18d6a6d66e55710e
# [20] https://www.semanticscholar.org/paper/73f972f488b154f3788364de76adfb9ff25ee436
# [21] https://www.semanticscholar.org/paper/76908d923308e74fabdc704dd42571e10488c0e6
# [22] https://www.semanticscholar.org/paper/4aea2eb267f33562b32a47bc9c876bae600ad25c
# [23] https://www.semanticscholar.org/paper/6ebba7a321a9159fc3b2f6dc8fd0777f7440fb01
# [24] https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4284979/
# [25] https://www.semanticscholar.org/paper/42152603b2546dc922485c1b1a0cb71378ddc309
# [26] https://www.semanticscholar.org/paper/01d31210f538f330b9c1e98ce83afa1bc19325b1
# [27] https://www.semanticscholar.org/paper/4f9f505caac311c1e5fd4d138adba4c88c69ce50
# [28] https://www.semanticscholar.org/paper/6b8a84a0732cf30960044523562a2da2fde53f23

# """

# # ================================
# # STEP 2: Extract Specific URLs
# # ================================
# # Define regular expressions to match arXiv and Semantic Scholar URLs.
# arxiv_pattern = r'https://arxiv.org/abs/\d+\.\d+'
# # semanticscholar_pattern = r'https://www.semanticscholar.org/paper/[^/]+/\w+'
# semanticscholar_pattern = r'https://www\.semanticscholar\.org/paper/(?:[^/]+/)?[\w-]+'


# # Extract URLs using the defined patterns.
# arxiv_urls = re.findall(arxiv_pattern, raw_text)
# semanticscholar_urls = re.findall(semanticscholar_pattern, raw_text)

# # Log the extracted URLs for debugging
# logging.basicConfig(filename='bibtex_extractor.log', level=logging.DEBUG, 
#                     format='%(asctime)s - %(levelname)s - %(message)s')

# logging.info(f"Extracted arXiv URLs: {arxiv_urls}")
# logging.info(f"Extracted Semantic Scholar URLs: {semanticscholar_urls}")

# # ================================
# # STEP 3: Define Fetch Functions for BibTeX
# # ================================
# def fetch_arxiv_bibtex(url):
#     """
#     Converts arXiv URL to its BibTeX representation by calling the bibtex endpoint.
#     """
#     try:
#         bib_url = url.replace('/abs/', '/bibtex/')  # Change the URL to BibTeX endpoint
#         response = requests.get(bib_url)
#         if response.status_code == 200:
#             bibtex = response.text.strip()
#             # Ensure the BibTeX entry ends with a closing brace
#             if not bibtex.endswith('}'):
#                 bibtex += '}'
#             return bibtex
#         else:
#             return f"% Failed to fetch BibTeX from {url} (Status code: {response.status_code})"
#     except Exception as e:
#         logging.error(f"Error fetching arXiv BibTeX for {url}: {str(e)}")
#         return f"% Error fetching arXiv BibTeX for {url}: {str(e)}"

# def fetch_semanticscholar_bibtex(url):
#     """
#     Extracts metadata from Semantic Scholar API and formats it as BibTeX.
#     """
#     try:
#         paper_id = url.split("/")[-1]  # Extract the paper ID from the URL
#         api_url = f"https://api.semanticscholar.org/graph/v1/paper/{paper_id}?fields=title,authors,year,venue,externalIds,url"
#         response = requests.get(api_url)

#         if response.status_code == 200:
#             data = response.json()
#             authors = " and ".join([author["name"] for author in data.get("authors", [])])
#             title = data.get("title", "Unknown Title")
#             journal = data.get("venue", "Unknown Journal")
#             year = data.get("year", "n.d.")
#             doi = data.get("externalIds", {}).get("DOI", None)

#             # Prepare BibTeX entry with DOI, URL, and open access file link
#             bibtex = (
#                 f"@article{{{paper_id},\n"
#                 f"  title={{ {title} }},\n"
#                 f"  author={{ {authors} }},\n"
#                 f"  journal={{ {journal} }},\n"
#                 f"  year={{ {year} }},\n"
#                 f"  doi={{ {doi} }},\n"
#                 f"  url={{ {data['url']} }}\n"
#                 f"}}"
#             )
#             return bibtex
#         else:
#             return f"% Failed to fetch from Semantic Scholar {url} (Status: {response.status_code})"
#     except Exception as e:
#         logging.error(f"Error fetching Semantic Scholar BibTeX for {url}: {str(e)}")
#         return f"% Error fetching Semantic Scholar BibTeX for {url}: {str(e)}"

# # Function to fetch BibTeX from Semantic Scholar using Selenium (for fallback)
# def fetch_semanticscholar_bibtex_selenium(url):
#     """
#     Scrapes BibTeX citation from Semantic Scholar using Selenium headless browser.
#     Used when API fails or browser-only data is needed.
#     """
#     options = Options()
#     options.add_argument("--headless")  # Run in headless mode (no GUI)
#     driver = webdriver.Chrome(options=options)  # Initialize Selenium driver
#     driver.get(url)  # Navigate to the Semantic Scholar paper page

#     time.sleep(3)  # Wait for the page to load completely

#     try:
#         # Click citation button
#         cite_button = driver.find_element(By.CSS_SELECTOR, 'button[data-heap-nav="citing-paper"]')
#         cite_button.click()
#         time.sleep(3)  # Wait for citation menu to open

#         # Switch to BibTeX tab
#         bibtex_tab = driver.find_element(By.XPATH, '//button[contains(text(), "BibTeX")]')
#         bibtex_tab.click()
#         time.sleep(3)  # Wait for BibTeX to load

#         # Extract BibTeX text
#         bibtex_text = driver.find_element(By.CSS_SELECTOR, "pre").text
#     except Exception as e:
#         logging.error(f"Error with Selenium: {e}")
#         bibtex_text = None
#     finally:
#         driver.quit()  # Close the Selenium browser

#     # Return as parsed BibTeX entry if found
#     if bibtex_text:
#         return bibtex_text.strip()
#     return None

# # ================================
# # STEP 4: Collect and Process Entries with Retry Logic
# # ================================
# # List to store all the BibTeX entries
# bib_entries = []

# # Function to implement the retry logic in case of 429 status
# def fetch_with_retry(url, fetch_func, retry_count=1):
#     """
#     Fetches the BibTeX data and retries with a delay if 429 error is encountered.
#     Implements exponential backoff to increase delay after each retry.
#     """
#     try:
#         response = fetch_func(url)  # Call the fetch function
#         # Retry if the status code is 429 (Too Many Requests)
#         if '429' in response:
#             print(f"Rate limit exceeded for {url}. Retrying after {7 * retry_count} seconds...")
#             time.sleep(7 * retry_count)  # Exponential backoff (increase the sleep time)
#             return fetch_with_retry(url, fetch_func, retry_count + 1)  # Retry the request with increased wait time
#         return response
#     except Exception as e:
#         logging.error(f"Error with URL {url}: {str(e)}")
#         return None

# # Process arXiv links
# for index, url in enumerate(arxiv_urls):
#     print(f"Fetching arXiv BibTeX for: {url}")
#     bib = fetch_with_retry(url, fetch_arxiv_bibtex)
#     if bib:
#         bib_entries.append(bib)
#     # Every 7 entries, pause for 7 seconds
#     if (index + 1) % 7 == 0:
#         print("Pausing for 7 seconds after processing 7 entries...")
#         time.sleep(7)

# # Process Semantic Scholar links
# if semanticscholar_urls:
#     for index, url in enumerate(semanticscholar_urls):
#         print(f"Fetching Semantic Scholar BibTeX for: {url}")
#         bib = fetch_with_retry(url, fetch_semanticscholar_bibtex)
#         if not bib:
#             # If API call fails, fall back to Selenium method
#             bib = fetch_with_retry(url, fetch_semanticscholar_bibtex_selenium)
#         if bib:
#             bib_entries.append(bib)
#         # Every 3 entries, pause for 7 seconds
#         if (index + 1) % 3 == 0:
#             print("Pausing for 3 seconds after processing 3 entries...")
#             time.sleep(7)
#         # Every 7 entries, pause for 7 seconds
#         if (index + 1) % 7 == 0:
#             print("Pausing for 7 seconds after processing 7 entries...")
#             time.sleep(7)
# else:
#     print("No Semantic Scholar URLs found. Skipping Semantic Scholar processing.")

# # ================================
# # STEP 5: Save Output to .bib File
# # ================================
# output_file = "BibTeX_output_with_doi_url.bib"
# try:
#     with open(output_file, "w", encoding="utf-8") as f:
#         for entry in bib_entries:
#             f.write(entry + "\n\n")
#     print(f"✅ BibTeX entries saved to '{output_file}'")
# except Exception as e:
#     logging.error(f"❌ Error writing to file: {e}")
#     sys.exit(1)




# """ import time
# import requests
# import re  # For regular expressions
# import sys  # For system exit on error
# from selenium import webdriver  # For Selenium scraping
# from selenium.webdriver.chrome.options import Options  # For Selenium settings
# from selenium.webdriver.common.by import By  # For locating elements in Selenium

# # ================================
# # STEP 1: Input Raw Text with URLs
# # ================================
# # Raw text containing all URLs.
# raw_text = """
# # Your list of URLs here
# """

# # ================================
# # STEP 2: Extract All URLs
# # ================================
# # This uses a regular expression to find and extract all URLs from the raw_text.
# all_urls = re.findall(r'https?://\S+', raw_text)

# # ================================
# # STEP 3: Filter arXiv and Semantic Scholar URLs
# # ================================
# # Filtering the URLs for specific domains:
# # 1. arXiv URLs (links that have "arxiv.org/abs/")
# arxiv_urls = [url for url in all_urls if "arxiv.org/abs/" in url]
# # 2. Semantic Scholar URLs (links that have "semanticscholar.org/paper/")
# semanticscholar_urls = [url for url in all_urls if "semanticscholar.org/paper/" in url]

# # ================================
# # STEP 4: Define Fetch Functions for BibTeX
# # ================================
# # Function to fetch BibTeX from arXiv URLs
# def fetch_arxiv_bibtex(url):
#     """
#     Converts arXiv URL to its BibTeX representation by calling the bibtex endpoint.
#     """
#     try:
#         bib_url = url.replace('/abs/', '/bibtex/')
#         response = requests.get(bib_url)
#         if response.status_code == 200:
#             bibtex = response.text.strip()
#             # Extract DOI from the URL if available
#             doi_match = re.search(r'http://doi.org/(10\.\d{4,9}/[-._;()/:A-Z0-9]+)', bibtex, re.IGNORECASE)
#             doi = doi_match.group(1) if doi_match else None
#             # Add DOI and URL to BibTeX entry
#             bibtex += f"\n  doi = {doi},\n  url = {url},\n"
#             return bibtex
#         else:
#             return f"% Failed to fetch BibTeX from {url} (Status code: {response.status_code})"
#     except Exception as e:
#         return f"% Error fetching arXiv BibTeX for {url}: {str(e)}"


# # Function to fetch BibTeX from Semantic Scholar URLs
# def fetch_semanticscholar_bibtex(url):
#     """
#     Extracts metadata from Semantic Scholar API and formats it as BibTeX, adding DOI, URL, and file link if open access.
#     """
#     try:
#         paper_id = url.split("/")[-1]
#         api_url = f"https://api.semanticscholar.org/graph/v1/paper/{paper_id}?fields=title,authors,year,venue,externalIds,url,openAccessPdf"
#         response = requests.get(api_url)

#         if response.status_code == 200:
#             data = response.json()
#             authors = " and ".join([author["name"] for author in data.get("authors", [])])
#             title = data.get("title", "Unknown Title")
#             journal = data.get("venue", "Unknown Journal")
#             year = data.get("year", "n.d.")
#             doi = data.get("externalIds", {}).get("DOI", None)
#             open_access_pdf = data.get("openAccessPdf", {}).get("url", None)

#             # Prepare BibTeX entry with DOI, URL, and open access file link
#             bibtex = (
#                 f"@article{{{paper_id},\n"
#                 f"  title={{ {title} }},\n"
#                 f"  author={{ {authors} }},\n"
#                 f"  journal={{ {journal} }},\n"
#                 f"  year={{ {year} }},\n"
#                 f"  doi={{ {doi} }},\n"
#                 f"  url={{ {data['url']} }},\n"
#                 f"  file={{ {open_access_pdf} }}\n"
#                 f"}}"
#             )
#             return bibtex
#         else:
#             return f"% Failed to fetch from Semantic Scholar {url} (Status: {response.status_code})"
#     except Exception as e:
#         return f"% Error fetching Semantic Scholar BibTeX for {url}: {str(e)}"


# # ================================
# # STEP 5: Collect and Process Entries with Retry Logic
# # ================================
# # List to store all the BibTeX entries
# bib_entries = []

# # Function to implement the retry logic in case of 429 status
# def fetch_with_retry(url, fetch_func):
#     """
#     Fetches the BibTeX data and retries with a delay if 429 error is encountered.
#     """
#     try:
#         response = fetch_func(url)
#         # Retry if the status code is 429 (Too Many Requests)
#         if '429' in response:
#             print(f"Rate limit exceeded for {url}. Retrying after 7 seconds...")
#             time.sleep(7)  # Sleep for 7 seconds before retrying
#             return fetch_with_retry(url, fetch_func)  # Retry the request
#         return response
#     except Exception as e:
#         print(f"Error with URL {url}: {str(e)}")
#         return None


# # Process arXiv links
# for index, url in enumerate(arxiv_urls):
#     print(f"Fetching arXiv BibTeX for: {url}")
#     bib = fetch_with_retry(url, fetch_arxiv_bibtex)
#     if bib:
#         bib_entries.append(bib)
#     # Every 7 entries, pause for 7 seconds
#     if (index + 1) % 3 == 0:
#         print("Pausing for 3 seconds after processing 3 entries...")
#         time.sleep(7)
#     if (index + 1) % 7 == 0:
#         print("Pausing for 7 seconds after processing 7 entries...")
#         time.sleep(7)

# # Process Semantic Scholar links
# for index, url in enumerate(semanticscholar_urls):
#     print(f"Fetching Semantic Scholar BibTeX for: {url}")
#     bib = fetch_with_retry(url, fetch_semanticscholar_bibtex)
#     if not bib:
#         # If API call fails, fall back to Selenium method
#         bib = fetch_with_retry(url, fetch_semanticscholar_bibtex_selenium)
#     if bib:
#         bib_entries.append(bib)
#     # Every 3 entries, pause for 7 seconds
#     if (index + 1) % 3 == 0:
#         print("Pausing for 3 seconds after processing 3 entries...")
#         time.sleep(7)
#     # Every 7 entries, pause for 7 seconds
#     if (index + 1) % 7 == 0:
#         print("Pausing for 7 seconds after processing 7 entries...")
#         time.sleep(7)

# # ================================
# # STEP 6: Save Output to .bib File
# # ================================
# output_file = "BibTeX_output_with_doi_url.bib"
# try:
#     with open(output_file, "w", encoding="utf-8") as f:
#         for entry in bib_entries:
#             f.write(entry + "\n\n")
#     print(f"✅ BibTeX entries saved to '{output_file}'")
# except Exception as e:
#     print(f"❌ Error writing to file: {e}")
#     sys.exit(1)
# """
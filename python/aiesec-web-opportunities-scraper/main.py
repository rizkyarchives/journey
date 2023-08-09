from opp_compiler import Compiler
from opp_analyzer import Analyzer
from data_uploader import Sheety

SHEET_LINK = 'https://api.sheety.co/9782b5927806d140b66f688283ba689e/opportunityCompiler/opportunities'
PUT_LINK_HERE = 'https://aiesec.org/search?earliest_start_date=2023-08-03&programmes=8'

compiler = Compiler()
analyzer = Analyzer()
uploader = Sheety(SHEET_LINK)

links = compiler.compile_link(PUT_LINK_HERE)

filtered_data = analyzer.analyze_link(links)

uploader.upload_data(filtered_data)





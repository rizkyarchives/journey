from opp_compiler import Compiler
from opp_analyzer import Analyzer
from data_uploader import Sheety

SHEET_LINK = '[Your Sheety API link]'
PUT_LINK_HERE = 'https://aiesec.org/search?earliest_start_date=2023-08-03&programmes=8'

compiler = Compiler()
analyzer = Analyzer()
uploader = Sheety(SHEET_LINK)

links = compiler.compile_link(PUT_LINK_HERE)

filtered_data = analyzer.analyze_link(links)

uploader.upload_data(filtered_data)





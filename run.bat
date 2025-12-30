pytest -s -v --browser_name=chrome testCases/ --html=reports/report_chrome.html --self-contained-html
REM pytest -s -v -m "sanity" --browser_name=chrome testCases/ --html=reports/report_chrome.html --self-contained-html
REM pytest -s -v -m "sanity or regression" --browser_name=chrome testCases/ --html=reports/report_chrome.html --self-contained-html
REM pytest -s -v -m "sanity and regression" --browser_name=chrome testCases/ --html=reports/report_chrome.html --self-contained-html
REM pytest -s -v -m "regression" --browser_name=chrome testCases/ --html=reports/report_chrome.html --self-contained-html

REM pytest -s -v -m "sanity" --browser_name=edge testCases/ --html=reports/report_edge.html --self-contained-html
REM pytest -s -v -m "sanity or regression" --browser_name=edge testCases/ --html=reports/report_edge.html --self-contained-html
REM pytest -s -v -m "sanity and regression" --browser_name=edge testCases/ --html=reports/report_edge.html --self-contained-html
REM pytest -s -v -m "regression" --browser_name=edge testCases/ --html=reports/report_edge.html --self-contained-html

REM pytest -s -v -m "sanity" --browser_name=firefox testCases/ --html=reports/report_firefox.html --self-contained-html
REM pytest -s -v -m "sanity or regression" --browser_name=firefox testCases/ --html=reports/report_firefox.html --self-contained-html
REM pytest -s -v -m "sanity and regression" --browser_name=firefox testCases/ --html=reports/report_firefox.html --self-contained-html
REM pytest -s -v -m "regression" --browser_name=firefox testCases/ --html=reports/report_firefox.html --self-contained-html

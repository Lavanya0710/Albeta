REM pytest -v -s -m "sanity" --html=Reports\sanityreport.html TestCases/
rem pytest -v -s -m "sanity and regression" --html=Reports\sanityandregressionreport.html TestCases/
rem pytest -v -s -m "sanity or regression" --html=Reports\sanityorregressionreport.html TestCases/ 
pytest -v -s -m "regression" --html=Reports\regressionreport.html TestCases/



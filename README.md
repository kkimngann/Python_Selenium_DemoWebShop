# Python_Selenium_DemoWebShop

**Supported browser: Chrome, Firefox**

**Steps to install and run test**

  Setup Python 3.10 and environment variable

  Open command line in folder root source code folder

  Setup Python packages: command "pip3 install -r requirements.txt"

1 - Update browser name at auto_test.cfg
  
2 - Run test: pytest --workers 2 --alluredir=allure-results test/steps_definition/test_login_steps.py 
  
3 - Wait for done
  
4 - Command to generate report: allure generate --clean
  
5 - Command to view report: allure open. The report will be show the summary and detail steps run
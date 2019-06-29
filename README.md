# govini-site-crawler
Simple python script to crawl a specified website to test to ensure results show up correctly from database

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing
purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them:

python 2.7
```
sudo apt update
sudo apt upgrade
sudo apt install python2.7 python-pip
```

Google Chrome & ChromeDriver - Follow the directions at the below website
```
https://tecadmin.net/setup-selenium-chromedriver-on-ubuntu/
```

### Installing

A step by step series of examples that tell you how to get a development env running

```
pip install virtualenv
git clone https://github.com/crherman7/govini-site-crawler.git
pip install -r requirements.txt
```

### Running the tests

A step by step series on how to run unit tests and integration tests

```
pip install -r test-requirements.txt
nosetests tests
nosetests integration_tests
```

### Deployment

A step by step series of examples that tell you how to get a production env running

```
git clone https://github.com/crherman7/govini-site-crawler.git
pip install -r requirements.txt
python setup.py install
```

### Run the code

A step by step series on how to run the code

```
run_crawler
```

The results will be similar to the following

```
==========
RESULTS
==========
{'program_number': u' 0603680F', 'file_name': u' U_0603680F_3_PB_2020', 'agency': u' Air Force', 'fiscal_year': u' 2020', 'budget_title': u' Advanced Technology Development (ATD)', 'program_title': u' Manufacturing Technology Program', 'appropriation_number': u' 3600'}
{'program_number': u' 0603680F', 'file_name': u' U_0603680F_3_PB_2019', 'agency': u' Air Force', 'fiscal_year': u' 2019', 'budget_title': u' Advanced Technology Development (ATD)', 'program_title': u' Manufacturing Technology Program', 'appropriation_number': u' 3600'}
{'program_number': u' 0603680F', 'file_name': u' U_0603680F_3_PB_2018', 'agency': u' Air Force', 'fiscal_year': u' 2018', 'budget_title': u' Advanced Technology Development (ATD)', 'program_title': u' Manufacturing Technology Program', 'appropriation_number': u' 3600'}
{'program_number': u' 0603680F', 'file_name': u' U_0603680F_3_PB_2017', 'agency': u' Air Force', 'fiscal_year': u' 2017', 'budget_title': u' Advanced Technology Development (ATD)', 'program_title': u' Manufacturing Technology Program', 'appropriation_number': u' 3600'}
{'program_number': u' 0603680F', 'file_name': u' 0603680F_3_PB_2016', 'agency': u' Air Force', 'fiscal_year': u' 2016', 'budget_title': u' Advanced Technology Development (ATD)', 'program_title': u' Manufacturing Technology Program', 'appropriation_number': u' 3600'}
{'program_number': u' 0603680F', 'file_name': u' 0603680F_3_PB_2015', 'agency': u' Air Force', 'fiscal_year': u' 2015', 'budget_title': u' Advanced Technology Development (ATD)', 'program_title': u' Manufacturing Technology Program', 'appropriation_number': u' 3600'}
{'program_number': u' 0603680F', 'file_name': u' 0603680F_3_PB_2014', 'agency': u' Air Force', 'fiscal_year': u' 2014', 'budget_title': u' Advanced Technology Development (ATD)', 'program_title': u' Manufacturing Technology Program', 'appropriation_number': u' 3600'}
{'program_number': u' 0603680F', 'file_name': u' 0603680F_3_PB_2013', 'agency': u' Air Force', 'fiscal_year': u' 2013', 'budget_title': u' Advanced Technology Development (ATD)', 'program_title': u' Manufacturing Technologies', 'appropriation_number': u' 3600'}
{'program_number': u' 0603680F', 'file_name': u' 0603680F_3_PB_2012', 'agency': u' Air Force', 'fiscal_year': u' 2012', 'budget_title': u' Advanced Technology Development (ATD)', 'program_title': u' Manufacturing Technologies', 'appropriation_number': u' 3600'}
{'program_number': u' 0603680F', 'file_name': u' 0603680F_PB_2011', 'agency': u' Air Force', 'fiscal_year': u' 2011', 'budget_title': u' Advanced Technology Development (ATD)', 'program_title': u' Manufacturing Technologies', 'appropriation_number': u' 3600'}
```
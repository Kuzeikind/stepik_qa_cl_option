import pytest

from selenium import webdriver

LANGUAGES_AVAILABLE = {
    'de' : 'German',
    'da' : 'Danish',
    'nl' : 'Dutch',
    'en-gb' : 'English',
    'it' : 'Italian',
    'es' : 'Spanish',
    'fr' : 'French',
    'ca' : 'Catalan',
    'pt' : 'Portugese',
    'pt-br' : 'Portugese (Brazilian)',
    'ro' : 'Romanian',
    'el' : 'Greek',
    'ru' : 'Russian',
    'pl' : 'Polish',
    'sl' : 'Slovenian',
    'uk' : 'Ukrainian',
    'cs' : 'Czech',
    'fi' : 'Finnish (Suomi)',
    'ar' : 'Arabic',
    'zh-cn' : 'Chinese (Traditional)',
    'ko' : 'Korean'
    }

def language_checker(lang):
	'''
	Check if the value of the --language option is valid.
	'''
	if lang not in LANGUAGES_AVAILABLE:
		raise pytest.UsageError(f'{lang} is not an available option')
	
	return lang


def pytest_addoption(parser):
	'''
	Add --language command line option.
	'''
	help_msg = 'Language ISO 639-1 code.\n' +\
		'Available languages: ' +\
		f'{[lang for lang in LANGUAGES_AVAILABLE]}'

	parser.addoption('--language',
                action='store',
                default='en-gb',
                help=help_msg,
                type=language_checker)


@pytest.fixture(scope='session')
def language(request):
	'''Return the language speicified in the command line.
	The language is set for the whole session.
	'''
	_language = request.config.getoption('language')
	return _language


@pytest.fixture(scope='class')
def browser():
	'''
	Set up a browser for tests.
	'''
	# Set up
	_browser = webdriver.Chrome()

	yield _browser
	# Tear down
	_browser.close()

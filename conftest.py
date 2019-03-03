import pytest
from fixture.application import Application


@pytest.fixture(scope="session")
def app(request):
    fixture = Application("C:\\FreeAddressBookPortable\\AddressBook.exe")
    request.addfinaliser(fixture.destroy)
    return fixture

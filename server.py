from case_no_file import CaseNoFile
from case_existing_file import CaseExistingFile
from case_directory_index_file import CaseDirectoryIndexFile
from case_default_file import CaseDefaultFile



Cases = [
    CaseNoFile(),
    CaseExistingFile(),          
    CaseDirectoryIndexFile(),
    CaseDefaultFile()
]
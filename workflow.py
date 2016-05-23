# Specify workflows from toplevel directory using GWF
# See http://mailund.github.io/gwf//

from gwf import *

# Obtain Data
target("Download_Data",
       output="data/housing.data") << '''
./scripts/getRawData.sh
'''


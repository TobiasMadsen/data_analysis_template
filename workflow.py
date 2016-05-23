# Specify workflows from toplevel directory using GWF
# See http://mailund.github.io/gwf//

from gwf import *

# Obtain Data
target("Download_Data",
       output="data/housing.data") << '''
./scripts/getRawData.sh
'''

# Do an analysis
target("Example_Analysis",
       input="data/housing.data",
       output=["analysis/some_analysis/some_analysis.html",
               "figures/price_age.png"]) << '''
(cd analysis/some_analysis/ && Rscript -e 'library(knitr); rmarkdown::render("some_analysis.Rmd")' )
'''

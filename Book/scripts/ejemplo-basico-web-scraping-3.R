install.packages("rvest")
install.packages("magrittr")

library("rvest")
library("magrittr")

rank_data <- html_nodes(html_doc, '.text-primary') %>%
             html_text()

title_data <- html_nodes(html_doc, '.lister-item-header a') %>%
              html_text()

head(rank_data)
head(title_data)



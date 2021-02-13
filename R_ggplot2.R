#https://ggplot2.tidyverse.org/
library(ggplot2)
cars <- read.csv("cars-sample.csv")

ggplot(data = cars, aes(x=Weight, y=MPG)) + geom_point()
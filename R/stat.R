library(ggplot2)

films <- read.csv('../csv/stat_basic.csv',header=TRUE,sep=',')
ggplot(films) + geom_bar(aes(x=key,y=value,fill=title),position = "dodge",stat='identity') + scale_fill_brewer(palette = "Set2") + labs(x='',y='') + theme(legend.title = element_blank(),axis.text.x = element_text(size = 15),axis.text.y = element_text(size = 15),legend.text = element_text(size = 15) ) 

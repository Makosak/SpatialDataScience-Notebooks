rm(list=ls())

#Open CSV, save as a new name
foreR<-read.csv("/Users/Masia/Downloads/IL_foreclosure\ 2/IL\ Tract.csv")
df<- as.data.frame(foreR)

head(foreR)

#note that the tract field was turned into integer from string, losing first three values
typeof(foreR$tract)
foreR$tractID<- substr(foreR$tractcode,6,11)
head(foreR)

df<- as.data.frame(foreR)

colnames(foreR) <- c("GEOID10","state","sta","county","countyname","tract","Hhun00","ForeN08","MortgN08","ForeRt08","VacntTot08","ResidTot08","VacnRt08","hiLn06","Ln06","hiLnRt06","Unemp08","HmDecl08","tractID")
head(foreR)
str(foreR)

df<- as.data.frame(foreR)
df[,7]
df[,1]
foreR$Hhun001<- as.numeric(as.character(df[,7]))
foreR$ForeRt081<- as.numeric(as.character(df[,8]))
foreR$VacnRt081<- as.numeric(as.character(df[,13]))
foreR$hiLnRt061<- as.numeric(as.character(df[,16]))
foreR$GEOID2<- as.numeric(as.character(df[,1]))


str(foreR)
head(foreR)

final<-as.data.frame(subset(foreR$GEOID10,foreR$Hhun00,foreR$ForeRt08,foreR$VacnRt08,foreR$hiLnRt06))
str(final)
final<-subset(foreR, select=c(foreR$GEOID10, foreR$Hhun00, foreR$ForeRt08, foreR$VacnRt08, foreR$hiLnRt06))



Hhun00<- as.integer(as.character(df[,7]))
Hhun00<- as.integer(as.character(df[,7]))
str(Hhun00)
head(df)

library(rgdal)
setwd("/Users/Masia/Desktop/desktop\ matter/FA_clip/Archive")
master<-readOGR(".","ACS_2010-2014_FoodAccess")
masterSD<-as.spatialdataframe(master)
as.sdata

head(master@data)

test<-merge(master,df,by="GEOID10",all.x = TRUE)
length(test)
head(test@data)

writeOGR(test, layer='test3', '/Users/Masia/Desktop', driver="ESRI Shapefile")

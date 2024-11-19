library(readxl)

myDF <- data.frame(read_xlsx(path = "./ds/CAL_Ingressantes_e_formados_por_sexo_test.xlsx"))
myDF2 <- data.frame(read_xls(path = "./ds/CCR Ingressantes e formados por sexo.xls"))

head(myDF)
head(myDF2)
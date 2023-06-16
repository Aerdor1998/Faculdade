#Arthur Pedroso De Francesco - RM551087
#Lucas Matheus da Silva - RM550466


#1 e #2
getwd()
install.packages("openxlsx")

library(openxlsx)


pre = read.xlsx("preacao.xlsx")
pos = read.xlsx("posacao.xlsx")

#3a
summary(pre)
summary(pos)
#b
predesp = pre$DESPERDÍCIO
posdesp = pos$DESPERDÍCIO
hist(predesp, col="blue", xlab="Desperdício em % dos alimentos totais", ylab="
     Quantos restaurantes se encaixam nos intervalos", main="Desperdício pré ações")
hist(posdesp, col="blue", xlab="Desperdício em % dos alimentos totais", ylab="
     Quantos restaurantes se encaixam nos intervalos", main="Desperdício pós ações")
#4
boxplot(pre$QTD.DE.ALIMENTOS.PROD., main="Qtd de alimentos produzidos (kg/dia) pré e pós ações",
        ylab="KG de alimentos produzidos em um dia", xlab="", col="white")


#5
posaval = pos$AVAL..DO.RESTAURANTE
preaval = pre$AVAL..DO.RESTAURANTE
resposta = table(preaval)
reposta = table(posaval)
9/30
10/30
11/30
pie(resposta, main="Avaliações dos restaurantes (pré-ações)", labels=c("30%","36,67%","33,33%"), col=c(4,2,3))
legend("topright",fill=c(4, 2, 3), legend=c("BOM", "MEDIO", "RUIM"))
14/30
12/30
4/30
pie(reposta, main="Avaliações dos restaurantes (pós-ações)", labels=c("46,67%","40%","13,33%"), col=c(4,2,3))
legend("topright",fill=c(4, 2, 3), legend=c("BOM", "MEDIO", "RUIM"))


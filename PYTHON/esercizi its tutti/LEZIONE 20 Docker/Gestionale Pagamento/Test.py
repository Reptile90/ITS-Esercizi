from PagamentoCartaDiCredito import PagamentoCartaDiCredito
from PagamentoContanti import PagamentoContanti

# Pagamenti in contanti
pagamentoContanti1 = PagamentoContanti()
pagamentoContanti1.setImporto(150.00)
pagamentoContanti1.inPezziDa()

pagamentoContanti2 = PagamentoContanti()
pagamentoContanti2.setImporto(95.20)
pagamentoContanti2.inPezziDa()

# Pagamenti con carta
pagamentoCarta1 = PagamentoCartaDiCredito("Mario Rossi", "12/24", "1234567890123456")
pagamentoCarta1.setImporto(200)

pagamentoCarta2 = PagamentoCartaDiCredito("Anna Bianchi", "11/26", "4111111111111111")
pagamentoCarta2.setImporto(75.50)

# Stampa dettagli
print(pagamentoContanti1.dettagliPagamento())
print(pagamentoContanti2.dettagliPagamento())
print(pagamentoCarta1.dettagliPagamento())
print(pagamentoCarta2.dettagliPagamento())

import requests

url = "http://example.com/api/resource"

# ============================================================
# GET
# ============================================================
# O método GET é usado para LER ou solicitar dados de um servidor.
# Ele NÃO envia corpo na requisição (apenas a URL e parâmetros).
# É o método mais comum — usado em navegação web.
# Quando bem-sucedido, o servidor retorna o código 200 (OK).
# Exemplo: buscar lista de usuários ou dados de um produto.
response = requests.get(url)
print("GET -> status:", response.status_code)
print("GET -> resposta:", response.text[:80], "\n")


# ============================================================
# HEAD
# ============================================================
# O método HEAD solicita SOMENTE os cabeçalhos (headers) de um recurso.
# Ele é igual ao GET, mas o corpo da resposta vem vazio.
# Útil para verificar metadados: tamanho, tipo, cookies, data de modificação, etc.
response = requests.head(url)
print("HEAD -> status:", response.status_code)
print("HEAD -> cabeçalhos:", dict(response.headers), "\n")


# ============================================================
# POST
# ============================================================
# O método POST é usado para ENVIAR dados ao servidor.
# Normalmente cria um novo recurso (registro, arquivo, etc).
# Os dados são enviados no corpo da requisição (formulário ou JSON).
# Quando bem-sucedido, o código é 201 (Created) ou 200 (OK).
# Exemplo: enviar formulário de cadastro.
data = {"nome": "João", "idade": 30}
response = requests.post(url, json=data)
print("POST -> status:", response.status_code)
print("POST -> corpo da resposta:", response.text[:80], "\n")


# ============================================================
# PUT
# ============================================================
# O método PUT serve para ATUALIZAR um recurso existente ou CRIAR um novo
# caso ele não exista.
# Ele substitui completamente os dados do recurso especificado.
# Exemplo: atualizar todo o cadastro de um usuário.
data_put = {"nome": "João Silva", "idade": 31}
response = requests.put(url + "/1", json=data_put)
print("PUT -> status:", response.status_code)
print("PUT -> corpo:", response.text[:80], "\n")


# ============================================================
# PATCH
# ============================================================
# O método PATCH é usado para atualizar PARCIALMENTE um recurso.
# Diferente do PUT, ele modifica apenas os campos enviados,
# mantendo o restante dos dados inalterados.
# Exemplo: atualizar apenas o nome do usuário.
data_patch = {"idade": 32}
response = requests.patch(url + "/1", json=data_patch)
print("PATCH -> status:", response.status_code)
print("PATCH -> corpo:", response.text[:80], "\n")


# ============================================================
# DELETE
# ============================================================
# O método DELETE é usado para REMOVER um recurso do servidor.
# Normalmente é seguido do ID do item que se deseja excluir.
# Quando bem-sucedido, o servidor retorna 200 (OK) ou 204 (No Content).
# Exemplo: deletar usuário de ID 1.
response = requests.delete(url + "/1")
print("DELETE -> status:", response.status_code, "\n")


# ============================================================
# OPTIONS
# ============================================================
# O método OPTIONS é utilizado para descobrir quais métodos HTTP
# são suportados para um determinado recurso.
# O servidor responde com o cabeçalho "Allow" listando os métodos disponíveis.
# Exemplo: usado por navegadores para verificar permissões CORS.
response = requests.options(url)
print("OPTIONS -> status:", response.status_code)
print("OPTIONS -> métodos permitidos:", response.headers.get("Allow"), "\n")


# ============================================================
# TRACE
# ============================================================
# O método TRACE serve para teste e depuração.
# Ele faz o servidor devolver exatamente o que recebeu da requisição (eco),
# permitindo analisar o caminho percorrido até o servidor.
# Útil para identificar erros em roteamento ou proxies.
response = requests.request("TRACE", url)
print("TRACE -> status:", response.status_code)
print("TRACE -> eco recebido:", response.text[:80], "\n")


# ============================================================
# CONNECT
# ============================================================
# O método CONNECT estabelece um túnel TCP/IP entre o cliente e o servidor.
# É amplamente usado para iniciar conexões HTTPS (criptografadas com SSL/TLS).
# Em Python 'requests' normalmente não é usado diretamente.
# Exemplo: usado por navegadores ao acessar sites HTTPS via proxy.
print("CONNECT -> cria um túnel TCP/IP para HTTPS (não usado diretamente em requests)\n")


# ============================================================
# COMPARAÇÃO GERAL
# ============================================================
print("========== COMPARAÇÃO ENTRE MÉTODOS ==========")
print("""
GET     → Lê dados do servidor (seguro e idempotente)
HEAD    → Lê apenas cabeçalhos (seguro e idempotente)
POST    → Cria um novo recurso (não idempotente)
PUT     → Atualiza ou cria um recurso (idempotente)
PATCH   → Atualiza parcialmente um recurso (não idempotente)
DELETE  → Remove um recurso (idempotente)
OPTIONS → Mostra métodos suportados (seguro e idempotente)
TRACE   → Eco para depuração (seguro e idempotente)
CONNECT → Cria túnel TCP (não idempotente, não seguro)
""")

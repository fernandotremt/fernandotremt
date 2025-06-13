### Hi there 👋

<!--
**fernandotremt/fernandotremt** is a ✨ _special_ ✨ repository because its `README.md` (this file) appears on your GitHub profile.

Here are some ideas to get you started:

- 🔭 I’m currently working on ...
- 🌱 I’m currently learning ...
- 👯 I’m looking to collaborate on ...
- 🤔 I’m looking for help with ...
- 💬 Ask me about ...
- 📫 How to reach me: ...
- 😄 Pronouns: ...
- ⚡ Fun fact: ...
-->

## Ferramentas de Acesso à Hemeroteca

Este repositório inclui um pequeno módulo em `tools/` para automatizar a
busca e a leitura de PDFs disponibilizados pela Hemeroteca Digital Brasileira.
Ele define três funções principais:

- `list_pdfs()`: lista os arquivos PDF encontrados no endereço base.
- `download_pdf(nome)`: baixa um PDF específico para o diretório desejado.
- `read_pdf_text(caminho)`: extrai o texto de um PDF local usando PyPDF2.

Para instalar as dependências, execute:

```bash
pip install -r requirements.txt
```

Depois importe as funções em seu projeto Python:

```python
from tools.hemeroteca_tools import list_pdfs, download_pdf, read_pdf_text
```

`list_pdfs` e `download_pdf` requerem acesso à internet para consultar o
servidor da Hemeroteca e baixar os arquivos correspondentes.

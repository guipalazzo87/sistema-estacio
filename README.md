# Projeto de Controle de Energia Condominial

## Descrição do Projeto

Este projeto visa implementar um sistema de controle e monitoramento de consumo de energia elétrica para um condomínio residencial. Utilizando tecnologias de IoT e Big Data, o sistema permite o controle remoto de equipamentos elétricos e fornece uma visualização detalhada do consumo de energia através de um dashboard interativo.

## Funcionalidades

- **Monitoramento de Energia:** Coleta e análise de dados de consumo de energia em tempo real.
- **Controle Remoto:** Controle de equipamentos elétricos como ar condicionado e luzes.
- **Dashboard Interativo:** Visualização gráfica dos dados de consumo com gráficos e relatórios.
- **Alertas e Notificações:** Notificações em caso de consumo anômalo ou excedente.

## Tecnologias Utilizadas

- **Linguagem:** Python
- **Bibliotecas:** Dash, Plotly, pandas
- **Dispositivos IoT:** ESP8266/ESP32, sensores de corrente
- **Banco de Dados:** SQLite (para dados locais), integração com serviços de nuvem

## Como Executar o Projeto

1. **Clone o Repositório:**

   ```bash
   git clone https://github.com/usuario/projeto-controle-energia.git
   cd projeto-controle-energia

   ```

2. **Instale as Dependências: Crie um ambiente virtual e instale as dependências listadas em requirements.txt:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```

3. **Configure o Ambiente: Siga as instruções no arquivo setup.sh para configurar os dispositivos IoT e a integração com a nuvem.**

Execute o Dashboard:

```bash
python codigo/dashboard.py
```

4. **Acesse o Dashboard: Abra o navegador e vá para <http://localhost:8050> para visualizar o dashboard.**

Exemplo de Uso
Controle de Ar Condicionado: Acesse o dashboard para ligar ou desligar o ar condicionado remotamente.
Monitoramento de Luzes: Verifique o consumo de energia das luzes em diferentes áreas do condomínio.

### Documentação Adicional

Diagrama de Arquitetura: Visualize a estrutura do sistema e a interação entre componentes.
Comentários do Código: Detalhes sobre a implementação e funcionalidades do código.

### Licença

Este projeto está licenciado sob a MIT License. Veja o arquivo LICENSE para mais detalhes.

### Contato

Para mais informações, entre em contato através desse repo!

### Links Adicionais

Dados de Exemplo: Dados de exemplo utilizados para testes.
Scripts de Teste: Scripts para validação e testes do sistema.

### Notas

1. **Substitua** `https://github.com/usuario/projeto-controle-energia.git` pelo URL real do seu repositório GitHub.
2. **Atualize** os nomes dos arquivos e pastas conforme sua estrutura real.
3. **Adapte** o texto para refletir exatamente as características do seu projeto e os requisitos específicos.

Se precisar de ajustes ou tiver mais perguntas, estou à disposição!

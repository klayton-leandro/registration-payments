# Plugin-based Payment Processing System

Este projeto implementa um sistema de processamento de pagamentos modular, orientado a plugins, que permite processar diferentes tipos de produtos e serviços. A arquitetura utiliza handlers específicos para cada tipo de pagamento e configurações dinâmicas definidas em arquivos YAML.

## Estrutura do Projeto

A estrutura do projeto é dividida em três camadas principais:

- **Camada de Configuração**: Define configurações específicas para cada tipo de produto em arquivos YAML.
- **Camada de Processamento**: Contém handlers responsáveis por processar diferentes tipos de pagamento.
- **Camada Principal (Core)**: O ponto de entrada do sistema, onde as configurações são carregadas e o processamento é orquestrado.

### Estrutura de Pastas

```plaintext
registerpayment/
├── adapters/
│   └── processor_adapter.py    # Classe base abstrata PaymentProcessor
├── bin/
│   ├── register_payment.py     # Função principal para registro de pagamentos
│   └── registration_payment.py # Funções adicionais de registro
├── config/
│   ├── book.yaml               # Configuração para pagamento de livros
│   ├── membership.yaml         # Configuração para assinatura
│   ├── membership_upgrade.yaml # Configuração para upgrade de assinatura
│   ├── physical_product.yaml   # Configuração para produtos físicos
│   └── skiing_video.yaml       # Configuração para vídeo de esqui
├── handlers/
│   ├── book_handler.py         # Handler para livros
│   ├── membership_handler.py   # Handler para assinatura
│   ├── membership_upgrade_handler.py # Handler para upgrade de assinatura
│   ├── physical_product_handler.py   # Handler para produtos físicos
│   └── skiing_video_handler.py       # Handler para vídeo de esqui
├── log/
│   └── book.log                # Arquivo de log de transações
├── main.py                     # Ponto de entrada da aplicação
└── utils/
    └── utils.py                # Utilitários de configuração e logging

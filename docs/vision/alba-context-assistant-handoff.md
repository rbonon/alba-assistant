# Alba Context Assistant — Handoff de Arquitetura e Implementação

**Data:** 2026-07-07  
**Autor/Contexto:** Ricardo Bonon — discussão consolidada com ChatGPT  
**Objetivo:** servir como documento único para continuar a implementação no Cursor/Claude Code.

---

## 1. Resumo executivo

A ideia discutida é evoluir a **Alba** para uma **assistente de contexto pessoal/familiar/profissional**, capaz de guardar, consultar e reaproveitar informações de diferentes fontes: notas humanas, pesquisas rápidas, receitas, decisões técnicas, documentos, repositórios Git, agenda e futuramente voz.

A decisão arquitetural principal é:

```text
Obsidian = memória humana e editável
Git = fonte da verdade técnica e código
Calendar/Tasks = fonte da verdade operacional de agenda e tarefas
Drive/Docs = documentos formais
RAG = índice inteligente e regenerável
MCP/API = porta padronizada para as IAs
Alba = assistente que usa tudo isso com contexto, permissões e personas
```

O RAG **não deve ser o local primário onde o conhecimento é armazenado**. Ele deve ser um **índice consultável** criado a partir das fontes canônicas.

---

## 2. Problema que a Alba resolve

Ricardo faz pequenas pesquisas e explorações com IA, como conversas sobre arquitetura, Obsidian, RAG, MCP, ferramentas de desenvolvimento, receitas, processos pessoais etc. Muitas dessas conversas têm valor futuro, mas se perdem em chats longos.

A Alba deve permitir:

- Capturar pesquisas e ideias rapidamente.
- Transformar conversas úteis em notas estruturadas.
- Consultar decisões antigas.
- Reaproveitar padrões técnicos e código existente.
- Guardar receitas e adaptações culinárias.
- Ajudar com textos, especialmente para Gisele.
- Preparar reuniões e tarefas a partir de contexto.
- Usar voz no Android ou Alexa como entrada opcional.
- Separar contextos de diferentes usuários: Ricardo, Gisele e Casa/Família.

---

## 3. Conceitos fundamentais

### 3.1 Obsidian

Obsidian é um app de notas baseado em arquivos Markdown locais. Ele é adequado para:

- Ideias.
- Pesquisas.
- Decisões.
- Receitas.
- Notas de projeto.
- Contextos pessoais.
- Templates.
- Rascunhos gerados por IA.

No projeto Alba, o Obsidian deve ser usado como **memória humana canônica**.

### 3.2 Git/GitHub

Os repositórios Git devem continuar sendo a fonte da verdade para:

- Código.
- README.
- Documentação técnica.
- `CLAUDE.md`.
- `AGENTS.md`.
- `.cursor/rules`.
- Scripts.
- Arquitetura formal dos projetos.

O Obsidian não deve copiar o repo inteiro. O RAG deve indexar os repositórios diretamente, com filtros.

### 3.3 RAG

RAG é a camada que recupera trechos relevantes de fontes externas antes de a IA responder.

Neste projeto:

```text
RAG = índice consultável e regenerável
```

Ele pode ser apagado e reconstruído a partir das fontes reais.

### 3.4 MCP/API

MCP ou API central funciona como a “tomada universal” para que diferentes clientes de IA consultem a memória.

Clientes possíveis:

- Cursor.
- Claude Code.
- ChatGPT.
- App próprio da Alba.
- Android voice.
- Alexa Skill.
- Scripts locais.

### 3.5 Assistente de contexto

A Alba não deve ser apenas um chatbot. Ela deve ser uma assistente que entende:

- Quem está usando.
- Qual contexto está ativo.
- Quais fontes pode consultar.
- Quais ferramentas pode executar.
- Qual tom/persona deve usar.

---

## 4. Princípios arquiteturais

### 4.1 Fonte da verdade ≠ índice

```text
Fonte da verdade:
  - Obsidian
  - Git
  - Calendar
  - Tasks
  - Drive

Índice:
  - Vector DB
  - Busca textual
  - Metadados
```

O índice RAG nunca deve ser a única cópia de uma informação importante.

### 4.2 A IA pode sugerir memória, mas não deve gravar direto sem controle

Fluxo recomendado:

```text
Conversa útil
  ↓
IA gera nota estruturada
  ↓
Salva em Inbox/AI Drafts
  ↓
Usuário revisa
  ↓
Move para pasta final
  ↓
RAG reindexa
```

### 4.3 Separação por usuário e contexto

Desde o início, toda nota/documento/embedding deve ter:

- `owner`
- `workspace`
- `visibility`
- `source`
- `type`
- `tags`

### 4.4 Busca híbrida

Para esse caso, busca apenas vetorial não basta.

Usar:

```text
Vector search + keyword/BM25 + metadata filters + reranking
```

Especialmente porque repositórios têm nomes exatos de funções, arquivos e comandos.

### 4.5 Começar read-only

A primeira versão deve consultar, resumir e gerar rascunhos. Escrita automática e ações operacionais devem vir depois.

---

## 5. Arquitetura alvo

```text
Interfaces
  ├── Web app Alba
  ├── Android app/voice capture
  ├── Alexa Skill, futuro
  ├── ChatGPT Voice, possível
  ├── Cursor
  └── Claude Code

        ↓

Alba API / MCP Server
  ├── autenticação
  ├── seleção de usuário/contexto
  ├── políticas de permissão
  ├── roteamento para ferramentas
  ├── acesso ao RAG
  └── criação de rascunhos

        ↓

RAG Layer
  ├── busca vetorial
  ├── busca textual
  ├── metadados
  ├── filtros por workspace
  ├── reranking
  └── referências às fontes

        ↓

Fontes canônicas
  ├── Obsidian Vaults
  ├── Git repositories
  ├── Google Calendar
  ├── Tasks/Todoist/Google Tasks
  ├── Google Drive
  └── Gmail, opcional e com cuidado
```

---

## 6. Multiusuário e multicontexto

A Alba deve suportar múltiplos contextos desde o início.

### 6.1 Workspaces iniciais

```text
workspace: ricardo
workspace: gisele
workspace: casa
workspace: compartilhado
```

### 6.2 Contexto Ricardo

Uso principal:

- Desenvolvimento de software.
- Arquitetura.
- IA.
- RAG/MCP.
- Repositórios Git.
- Padrões de UI.
- Decisões técnicas.
- Documentação para Cursor/Claude.
- Pesquisas técnicas.

Persona sugerida:

```text
Alba Dev
= objetiva, técnica, estruturada, orientada a implementação.
```

Ferramentas permitidas:

- Buscar em Git.
- Buscar em Obsidian/Ricardo.
- Consultar padrões.
- Gerar documentação técnica.
- Gerar prompts/CLAUDE.md.
- Encontrar código reaproveitável.

### 6.3 Contexto Gisele

Uso principal:

- Tratamento de texto.
- Reescrita.
- Organização de ideias.
- Estudos.
- Materiais de psicanálise/virtologia.
- Textos profissionais.

Persona sugerida:

```text
Alba Texto
= clara, cuidadosa, acolhedora, boa editora, preserva voz da autora.
```

Ferramentas permitidas:

- Reescrever texto.
- Ajustar tom.
- Resumir estudo.
- Transformar anotações em material organizado.
- Criar rascunhos.

Observação importante:

Conteúdo clínico sensível, dados de pacientes ou dados identificáveis de saúde mental devem ficar fora do MVP ou em área isolada, criptografada e com regras de privacidade rigorosas.

### 6.4 Contexto Casa/Família

Uso principal:

- Receitas.
- Listas.
- Tarefas domésticas.
- Viagens.
- Documentos familiares.
- Agenda compartilhada.

Persona sugerida:

```text
Alba Casa
= prática, simples, útil no dia a dia.
```

Ferramentas permitidas:

- Buscar receitas.
- Criar lista.
- Criar rascunho de tarefa.
- Preparar briefing de evento.
- Consultar documentos domésticos autorizados.

### 6.5 Regras de acesso

```text
Ricardo pode consultar:
  - workspace ricardo
  - workspace casa
  - workspace compartilhado

Gisele pode consultar:
  - workspace gisele
  - workspace casa
  - workspace compartilhado

Casa pode consultar:
  - workspace casa
  - workspace compartilhado
```

Não misturar contextos privados por padrão.

---

## 7. Modelo de dados mínimo

### 7.1 Documento indexado

```ts
export type IndexedDocument = {
  id: string;
  owner: 'ricardo' | 'gisele' | 'shared';
  workspace: 'ricardo' | 'gisele' | 'casa' | 'compartilhado';
  visibility: 'private' | 'shared' | 'restricted';
  source: 'obsidian' | 'git' | 'calendar' | 'task' | 'drive' | 'gmail' | 'manual';
  sourcePath?: string;
  repo?: string;
  title: string;
  type:
    | 'research_note'
    | 'decision'
    | 'recipe'
    | 'project_note'
    | 'coding_standard'
    | 'source_code'
    | 'meeting_context'
    | 'task'
    | 'document'
    | 'draft';
  tags: string[];
  createdAt?: string;
  updatedAt?: string;
  contentHash: string;
};
```

### 7.2 Chunk indexado

```ts
export type IndexedChunk = {
  id: string;
  documentId: string;
  chunkIndex: number;
  text: string;
  embedding?: number[];
  metadata: {
    owner: string;
    workspace: string;
    source: string;
    sourcePath?: string;
    repo?: string;
    type: string;
    tags: string[];
    priority: 'high' | 'medium' | 'low';
  };
};
```

### 7.3 Perfil de usuário

```ts
export type AlbaUser = {
  id: 'ricardo' | 'gisele';
  displayName: string;
  defaultWorkspace: string;
  allowedWorkspaces: string[];
  defaultPersona: string;
};
```

### 7.4 Persona

```ts
export type AlbaPersona = {
  id: 'alba_dev' | 'alba_texto' | 'alba_casa';
  name: string;
  tone: string;
  allowedTools: string[];
  defaultRetrievalFilters: Record<string, unknown>;
};
```

---

## 8. Estrutura sugerida de vaults

### 8.1 Opção simples: um vault com pastas separadas

```text
AlbaVault/
  00 Inbox/
    AI Drafts/
    Quick Notes/

  10 Ricardo/
    Pesquisas/
    Projetos/
    Decisoes/
    Padroes/
    IA/

  20 Gisele/
    Textos/
    Estudos/
    Rascunhos/
    Referencias/

  30 Casa/
    Receitas/
    Documentos/
    Viagens/
    Tarefas/

  40 Compartilhado/
    Familia/
    Receitas/
    AgendaContext/

  90 Templates/
    pesquisa.md
    receita.md
    decisao.md
    projeto.md
    texto.md
```

### 8.2 Opção mais isolada: múltiplos vaults

```text
AlbaData/
  vaults/
    ricardo/
    gisele/
    casa/
    compartilhado/

  rag-index/
    ricardo/
    gisele/
    casa/
    compartilhado/
```

Para MVP familiar, a primeira opção é mais simples. Para privacidade mais forte, usar múltiplos vaults.

---

## 9. Templates de notas

### 9.1 Template de pesquisa

```md
# Pesquisa: {{title}}

## Resumo

## Contexto

## Principais conclusões

## Decisões tomadas

## Próximas ações

## Fontes / links

## Status
- [ ] Revisar
- [ ] Implementar
- [ ] Arquivar

## Tags
#pesquisa
```

### 9.2 Template de decisão

```md
# Decisão: {{title}}

## Data
{{date}}

## Contexto

## Opções consideradas

## Decisão

## Motivo

## Consequências

## Revisar quando

## Tags
#decisao
```

### 9.3 Template de receita

```md
# Receita: {{title}}

## Contexto

## Ingredientes

## Modo de preparo

## O que funcionou

## Ajustes para próxima vez

## Variações

## Tags
#receita
```

### 9.4 Template de projeto

```md
# Projeto: {{title}}

## Objetivo

## Status atual

## Repositórios relacionados

## Decisões importantes

## Arquitetura resumida

## Próximas ações

## Links úteis

## Tags
#projeto
```

### 9.5 Template de texto para Gisele

```md
# Texto: {{title}}

## Objetivo do texto

## Público

## Tom desejado

## Rascunho original

## Versão trabalhada

## Observações

## Tags
#texto
```

---

## 10. Pipeline de ingestão/indexação

### 10.1 Fontes iniciais

MVP deve indexar:

```text
Obsidian:
  - .md

Git:
  - README.md
  - CLAUDE.md
  - AGENTS.md
  - docs/**/*.md
  - package.json
  - src/**/*.{ts,tsx,js,jsx,py}
```

Excluir:

```text
node_modules/
dist/
build/
.git/
.env
.env.*
*.log
coverage/
.cache/
.next/
out/
```

### 10.2 Etapas do indexador

```text
1. Descobrir arquivos
2. Aplicar filtros
3. Ler conteúdo
4. Normalizar texto
5. Detectar metadados
6. Dividir em chunks
7. Gerar embeddings
8. Atualizar banco vetorial
9. Atualizar índice textual
10. Registrar origem e hash
```

### 10.3 Prioridades de indexação

Alta prioridade:

```text
Obsidian/Decisoes
Obsidian/Padroes
Obsidian/Projetos
repo/CLAUDE.md
repo/AGENTS.md
repo/README.md
repo/docs
```

Média prioridade:

```text
src/components
src/lib
src/services
package.json
scripts
```

Baixa prioridade:

```text
Inbox
rascunhos
notas soltas
conversas importadas
```

---

## 11. Ferramentas da Alba API/MCP

### 11.1 Ferramentas read-only iniciais

```ts
search_memory(query, filters)
get_project_context(projectName)
get_decisions(topic)
get_standards(area)
search_repos(query, filters)
find_reusable_code(description)
find_recipe(query)
```

### 11.2 Ferramentas de escrita controlada

```ts
save_note_draft(title, content, workspace)
save_research_draft(title, content, workspace)
save_recipe_draft(title, content, workspace)
save_decision_draft(title, content, workspace)
summarize_conversation_to_draft(conversation, workspace)
```

Todas devem salvar inicialmente em:

```text
00 Inbox/AI Drafts/
```

### 11.3 Ferramentas futuras de ação

```ts
create_task(title, dueDate, workspace)
create_calendar_event(title, start, end, attendees)
prepare_meeting(eventId)
read_calendar_context(dateRange)
search_drive(query)
```

---

## 12. Fluxos principais

### 12.1 Capturar pesquisa feita com IA

```text
1. Ricardo conversa com IA sobre um assunto.
2. Ao final, pede: “salve isso como pesquisa”.
3. Alba gera nota estruturada.
4. Nota vai para Inbox/AI Drafts.
5. Ricardo revisa e move para Pesquisas/ ou Decisoes/.
6. Indexador reprocessa.
7. Futuras IAs conseguem consultar.
```

### 12.2 Consultar decisões antigas

```text
Pergunta:
“O que eu já decidi sobre RAG, Obsidian e MCP?”

Fluxo:
1. search_memory()
2. Busca nos workspaces autorizados.
3. Retorna notas de pesquisa, decisões e projeto.
4. Alba responde com síntese e links para arquivos.
```

### 12.3 Reaproveitar código

```text
Pergunta:
“Onde eu já fiz upload de documento com validação humana?”

Fluxo:
1. search_repos()
2. Busca textual por upload, receipt, document, validation.
3. Busca vetorial por significado.
4. Retorna arquivos e trechos relevantes.
5. Alba sugere reaproveitamento.
```

### 12.4 Receita culinária

```text
Pergunta:
“Tenho frango seco e não quero usar creme de leite. O que já fiz antes?”

Fluxo:
1. find_recipe()
2. Busca em Casa/Receitas e Ricardo/Receitas.
3. Retorna receita adaptada e variações.
```

### 12.5 Preparar reunião

```text
Pergunta:
“Prepare minha reunião de amanhã sobre Alba Docs.”

Fluxo futuro:
1. Calendar identifica evento.
2. RAG busca contexto em Projetos/Alba.
3. Git busca status técnico.
4. Alba gera briefing.
```

---

## 13. Voz: Android e Alexa

### 13.1 Decisão

Ricardo não tem iPhone. As interfaces mais práticas são:

```text
Android = captura pessoal principal
Alexa = comandos domésticos curtos
ChatGPT Voice = conversa longa, se integrado ao MCP
```

Google Assistant/Gemini pode ser útil como assistente geral do Android, mas não parece a melhor base para customização profunda do sistema próprio.

### 13.2 Arquitetura Android

```text
Android app
  ↓ fala
Speech-to-text
  ↓ texto
Alba API
  ↓
Obsidian Inbox / RAG / Tasks / Calendar
```

MVP Android:

- Botão “Falar”.
- Transcrição.
- Seleção de tipo: pesquisa, receita, tarefa, nota rápida.
- Envio para `/capture`.
- Salvamento como Markdown em `00 Inbox/AI Drafts`.

### 13.3 Arquitetura Alexa

```text
Alexa Device
  ↓
Alexa Skill
  ↓
Webhook/Lambda
  ↓
Alba API
  ↓
RAG / Obsidian / Tasks
```

Usos bons para Alexa:

- “Salvar receita rápida.”
- “Adicionar item na lista.”
- “Consultar uma receita.”
- “Criar lembrete simples.”

Usos ruins para Alexa:

- Exploração técnica longa.
- Discussões complexas.
- Geração extensa de documentação.

---

## 14. Agenda, tarefas e documentos

### 14.1 Agenda

Agenda real deve ficar em:

```text
Google Calendar / Outlook / Apple Calendar
```

Obsidian pode guardar contexto de reuniões, não a agenda em si.

### 14.2 Tarefas

Tarefas com data, recorrência e cobrança devem ficar em ferramenta própria:

```text
Google Tasks / Todoist / Apple Reminders / Linear / Jira
```

Obsidian pode guardar checklists e tarefas contextuais leves.

### 14.3 Documentos

Documentos formais devem ficar em:

```text
Google Drive / filesystem / storage próprio
```

RAG indexa metadados e conteúdo permitido.

---

## 15. Segurança, privacidade e LGPD

### 15.1 Regra geral

Separar fortemente:

```text
Conteúdo pessoal comum
Conteúdo técnico
Conteúdo familiar compartilhado
Conteúdo sensível
```

### 15.2 Conteúdo clínico ou sensível da Gisele

Para MVP:

```text
Não indexar conteúdo clínico sensível.
Não armazenar dados identificáveis de pacientes.
Não misturar em RAG geral.
```

Futuro, se necessário:

```text
- workspace separado
- criptografia
- anonimização
- controle de acesso
- logs de acesso
- política de retenção
- opção de exclusão
```

### 15.3 Segredos em repositórios

Nunca indexar:

```text
.env
.env.*
secrets.json
credentials.json
keys
certificados privados
tokens
```

---

## 16. Stack técnica sugerida

### 16.1 MVP simples

```text
Backend:
  Node.js/TypeScript ou Python/FastAPI

Armazenamento:
  filesystem + SQLite

Vector DB:
  Chroma, LanceDB ou Qdrant local

Busca textual:
  SQLite FTS5 ou Tantivy/Meilisearch, futuro

Framework RAG:
  LlamaIndex ou LangChain

Interface inicial:
  CLI + API HTTP

Integração dev:
  MCP server para Cursor/Claude
```

### 16.2 Alternativa mais robusta

```text
Backend:
  TypeScript + Fastify/NestJS

DB:
  PostgreSQL + pgvector

Busca:
  PostgreSQL full text ou Meilisearch

Queue:
  BullMQ/Redis, futuro

Auth:
  local auth simples no MVP
```

### 16.3 Escolha recomendada para começar

Para começar rápido no Cursor:

```text
TypeScript + Node.js
SQLite para metadados
LanceDB ou Chroma para vetores
Express/Fastify para API
MCP server separado ou no mesmo projeto
```

Motivo: aproxima do ecossistema de desenvolvimento web/app que Ricardo já usa.

---

## 17. Estrutura inicial de repositório

```text
alba-assistant/
  README.md
  CLAUDE.md
  package.json
  .env.example
  .gitignore

  src/
    config/
      paths.ts
      workspaces.ts
      personas.ts

    core/
      types.ts
      permissions.ts
      metadata.ts

    ingestion/
      fileDiscovery.ts
      obsidianLoader.ts
      gitLoader.ts
      chunker.ts
      embedder.ts
      indexer.ts

    retrieval/
      vectorSearch.ts
      keywordSearch.ts
      hybridSearch.ts
      reranker.ts

    tools/
      searchMemory.ts
      getProjectContext.ts
      getDecisions.ts
      getStandards.ts
      findRecipe.ts
      saveDraft.ts

    api/
      server.ts
      routes.ts

    mcp/
      server.ts
      tools.ts

    writers/
      markdownWriter.ts
      draftWriter.ts

    security/
      filters.ts
      secretScanner.ts

  scripts/
    index-obsidian.ts
    index-git.ts
    reindex-all.ts
    dev-server.ts

  data/
    .gitkeep

  docs/
    architecture.md
    roadmap.md
    data-model.md
```

---

## 18. Configuração de workspaces

Exemplo:

```ts
export const workspaces = {
  ricardo: {
    owner: 'ricardo',
    rootPath: '/Users/ricardo/AlbaData/vaults/ricardo',
    allowedUsers: ['ricardo'],
    defaultPersona: 'alba_dev',
  },
  gisele: {
    owner: 'gisele',
    rootPath: '/Users/ricardo/AlbaData/vaults/gisele',
    allowedUsers: ['gisele'],
    defaultPersona: 'alba_texto',
  },
  casa: {
    owner: 'shared',
    rootPath: '/Users/ricardo/AlbaData/vaults/casa',
    allowedUsers: ['ricardo', 'gisele'],
    defaultPersona: 'alba_casa',
  },
};
```

---

## 19. API HTTP inicial

### 19.1 Buscar memória

```http
POST /memory/search
```

Body:

```json
{
  "userId": "ricardo",
  "workspace": "ricardo",
  "query": "o que eu decidi sobre Obsidian RAG MCP?",
  "filters": {
    "types": ["research_note", "decision", "project_note"]
  }
}
```

### 19.2 Salvar rascunho

```http
POST /drafts
```

Body:

```json
{
  "userId": "ricardo",
  "workspace": "ricardo",
  "type": "research_note",
  "title": "Obsidian, RAG e MCP como memória pessoal",
  "content": "..."
}
```

### 19.3 Buscar receita

```http
POST /recipes/search
```

Body:

```json
{
  "userId": "ricardo",
  "query": "molho quente para frango seco sem creme de leite"
}
```

---

## 20. MCP tools iniciais

```ts
const tools = [
  {
    name: 'search_memory',
    description: 'Search Alba memory across allowed workspaces.',
  },
  {
    name: 'get_project_context',
    description: 'Retrieve project context from notes and repos.',
  },
  {
    name: 'get_decisions',
    description: 'Find prior decisions about a topic.',
  },
  {
    name: 'get_standards',
    description: 'Retrieve Ricardo coding or writing standards.',
  },
  {
    name: 'find_recipe',
    description: 'Find recipes and cooking notes.',
  },
  {
    name: 'save_note_draft',
    description: 'Save a draft note to the correct Inbox/AI Drafts folder.',
  },
];
```

---

## 21. Roadmap de implementação

### Fase 0 — Preparação conceitual

- [ ] Criar repositório `alba-assistant`.
- [ ] Criar este documento em `docs/architecture.md`.
- [ ] Definir local das pastas/vaults.
- [ ] Definir nomes dos workspaces.
- [ ] Criar `.env.example`.

### Fase 1 — Obsidian manual

- [ ] Criar estrutura de vault.
- [ ] Criar templates de pesquisa, decisão, receita e projeto.
- [ ] Começar captura manual de notas.
- [ ] Salvar esta discussão como primeira pesquisa.

Critério de sucesso:

```text
Ricardo consegue criar e consultar manualmente notas estruturadas no Obsidian.
```

### Fase 2 — Indexador read-only

- [ ] Implementar file discovery.
- [ ] Ler Markdown do Obsidian.
- [ ] Ler README/CLAUDE/docs de repos Git.
- [ ] Criar chunks.
- [ ] Gerar embeddings.
- [ ] Salvar metadados.
- [ ] Criar busca simples.

Critério de sucesso:

```text
Uma pergunta sobre “Obsidian RAG MCP” retorna as notas corretas.
```

### Fase 3 — Busca híbrida

- [ ] Adicionar busca textual.
- [ ] Combinar score vetorial + textual.
- [ ] Filtrar por workspace.
- [ ] Retornar fontes e paths.

Critério de sucesso:

```text
Busca por termos exatos como CLAUDE.md, repo_init e rbo-ui-tokenize funciona bem.
```

### Fase 4 — API local

- [ ] Criar `/memory/search`.
- [ ] Criar `/drafts`.
- [ ] Criar `/recipes/search`.
- [ ] Criar autenticação simples ou user selector.

Critério de sucesso:

```text
Um cliente externo consegue consultar e salvar rascunho.
```

### Fase 5 — MCP server

- [ ] Expor `search_memory`.
- [ ] Expor `get_project_context`.
- [ ] Expor `get_decisions`.
- [ ] Expor `find_recipe`.
- [ ] Testar no Cursor/Claude.

Critério de sucesso:

```text
Cursor consegue perguntar à Alba sobre decisões e padrões pessoais.
```

### Fase 6 — Escrita controlada

- [ ] Implementar `save_research_draft`.
- [ ] Implementar `save_recipe_draft`.
- [ ] Implementar `save_decision_draft`.
- [ ] Garantir que tudo vá para Inbox/AI Drafts.

Critério de sucesso:

```text
Após uma conversa, a IA gera nota revisável no Obsidian.
```

### Fase 7 — Android voice capture

- [ ] Criar app simples ou automação Android.
- [ ] Capturar fala.
- [ ] Transcrever.
- [ ] Enviar para API.
- [ ] Salvar rascunho.

Critério de sucesso:

```text
Ricardo fala uma pesquisa curta no Android e ela aparece como Markdown no Inbox.
```

### Fase 8 — Alexa, futuro

- [ ] Criar Alexa Skill.
- [ ] Integrar webhook/Lambda.
- [ ] Restringir a comandos curtos.
- [ ] Testar receitas/listas/notas rápidas.

---

## 22. Primeiras histórias de usuário

### 22.1 Ricardo salva pesquisa

```text
Como Ricardo,
quero transformar uma conversa útil com IA em uma nota de pesquisa,
para recuperar e implementar depois.
```

Aceite:

- Gera Markdown estruturado.
- Salva em `00 Inbox/AI Drafts`.
- Inclui resumo, decisões e próximas ações.

### 22.2 Ricardo consulta decisão técnica

```text
Como Ricardo,
quero perguntar o que já decidi sobre um assunto,
para não repetir discussões antigas.
```

Aceite:

- Busca no workspace `ricardo`.
- Retorna notas relevantes.
- Mostra paths das fontes.

### 22.3 Ricardo encontra código reaproveitável

```text
Como Ricardo,
quero encontrar onde já implementei algo parecido,
para reaproveitar padrões ou código.
```

Aceite:

- Busca em repos autorizados.
- Ignora `node_modules`, build e secrets.
- Retorna arquivos e resumo.

### 22.4 Gisele trata texto

```text
Como Gisele,
quero transformar anotações em um texto claro,
para usar em estudos ou materiais profissionais.
```

Aceite:

- Usa persona `Alba Texto`.
- Não consulta workspace Ricardo.
- Salva rascunho no workspace Gisele.

### 22.5 Casa consulta receita

```text
Como usuário da casa,
quero consultar uma receita que já funcionou,
para repetir ou adaptar.
```

Aceite:

- Busca em receitas compartilhadas.
- Retorna variações e observações.

---

## 23. Decisões já tomadas nesta discussão

1. Alba deve ser uma assistente de contexto, não apenas um repositório de documentos.
2. Obsidian é adequado para memória humana: pesquisas, ideias, receitas, decisões e notas.
3. Git continua sendo a fonte da verdade para software.
4. Repositórios podem fazer parte da memória consultável, mas não devem ser copiados integralmente para o Obsidian.
5. RAG deve indexar Obsidian + Git + documentos autorizados.
6. RAG não é storage primário; é índice regenerável.
7. MCP/API central deve ser a camada de acesso para Cursor, Claude, ChatGPT e outros clientes.
8. Escrita por IA deve começar como rascunho revisável.
9. Android é melhor ponto inicial para captura por voz, já que Ricardo não tem iPhone.
10. Alexa é viável para comandos domésticos curtos.
11. Google Assistant/Gemini não deve ser a base principal de customização no início.
12. A arquitetura deve nascer multiusuário/multicontexto.
13. Workspaces iniciais: Ricardo, Gisele, Casa e Compartilhado.
14. Persona Ricardo deve ser técnica/dev.
15. Persona Gisele deve focar em tratamento de texto e organização de ideias.
16. Conteúdo clínico sensível deve ficar fora do MVP.
17. Agenda deve ficar em Calendar; Obsidian guarda contexto, não a agenda principal.
18. Tarefas com cobrança devem ficar em ferramenta própria; Obsidian guarda tarefas contextuais leves.

---

## 24. Riscos e mitigação

### 24.1 Memória virar bagunça

Mitigação:

- Usar templates.
- Salvar IA em Inbox/Drafts.
- Revisar antes de promover.
- Usar tags e tipos.

### 24.2 Misturar contextos de usuários

Mitigação:

- Workspace obrigatório.
- Filtros de permissão em todas as buscas.
- Índices separados ou namespaces.

### 24.3 Indexar segredo de repo

Mitigação:

- Lista forte de exclusão.
- Secret scanner.
- Nunca indexar `.env`.

### 24.4 Conteúdo sensível da Gisele

Mitigação:

- Fora do MVP.
- Workspace separado e restrito, se necessário no futuro.

### 24.5 Excesso de complexidade

Mitigação:

- Começar read-only.
- Primeiro Obsidian + Git local.
- Depois API.
- Depois MCP.
- Depois voz.

---

## 25. Próximo passo recomendado no Cursor

Criar o repositório `alba-assistant` com este objetivo inicial:

```text
Construir um MVP local read-only que indexa notas Markdown do Obsidian e arquivos selecionados de repositórios Git, permitindo busca híbrida filtrada por workspace.
```

Prompt inicial para Cursor:

```text
You are helping me implement Alba Context Assistant.

Goal for MVP:
Build a local TypeScript project that indexes Markdown notes from an Obsidian vault and selected files from Git repositories, stores metadata and embeddings, and exposes a simple API for hybrid memory search.

Important architectural decisions:
- Obsidian is the canonical human memory.
- Git is the canonical technical/code memory.
- RAG is a regenerable index, not the source of truth.
- The system must support multiple workspaces: ricardo, gisele, casa, compartilhado.
- All search must be filtered by allowed workspaces.
- AI-generated writes must go to Inbox/AI Drafts only.
- Do not index secrets, .env files, node_modules, build outputs, or sensitive clinical material.

Start by creating:
- project structure
- TypeScript types
- workspace config
- file discovery
- Markdown loader
- git loader with exclusion rules
- chunker
- placeholder embedding interface
- simple metadata store
- search API skeleton
```

---

## 26. Primeira nota a salvar no Obsidian

Sugestão de arquivo:

```text
AlbaVault/10 Ricardo/Pesquisas/alba-assistant-assistant-rag-mcp.md
```

Conteúdo sugerido:

```md
# Alba Context Assistant com Obsidian, Git, RAG e MCP

## Resumo

Quero desenvolver a Alba como uma assistente de contexto pessoal/familiar/profissional. Ela deve consultar notas humanas, repositórios Git, receitas, documentos e futuramente agenda e tarefas.

## Decisões principais

- Obsidian será a memória humana.
- Git continuará sendo a fonte da verdade técnica.
- RAG será o índice consultável e regenerável.
- MCP/API será a interface para Cursor, Claude, ChatGPT e apps.
- A Alba deve nascer com suporte a múltiplos workspaces.
- A escrita da IA deve começar como rascunho em Inbox/AI Drafts.

## Workspaces iniciais

- Ricardo: software, IA, arquitetura, decisões técnicas.
- Gisele: textos, estudos, organização de ideias.
- Casa: receitas, documentos, tarefas domésticas.
- Compartilhado: contexto familiar comum.

## Próximas ações

- Criar repo alba-assistant.
- Criar estrutura de vault.
- Implementar indexador read-only.
- Implementar busca híbrida.
- Expor API local.
- Depois criar MCP.
```

---

## 27. Glossário

### Alba

Nome da assistente/plataforma de contexto.

### Workspace

Espaço lógico de conhecimento e permissão. Exemplos: Ricardo, Gisele, Casa.

### Persona

Modo de resposta e conjunto de ferramentas. Exemplos: Alba Dev, Alba Texto, Alba Casa.

### Obsidian Vault

Pasta de arquivos Markdown usada como memória humana.

### RAG

Retrieval-Augmented Generation. Técnica para buscar contexto externo antes da IA responder.

### MCP

Model Context Protocol. Padrão para conectar modelos de IA a ferramentas e fontes externas.

### Fonte canônica

Local onde o dado realmente vive. Exemplo: Git para código, Obsidian para notas.

### Índice regenerável

Banco de busca que pode ser reconstruído a partir das fontes canônicas.

---

## 28. Conclusão

A ideia é viável, útil e alinhada ao uso real de Ricardo e Gisele.

A Alba deve começar simples:

```text
Obsidian + Git + RAG read-only + API local
```

Depois evoluir para:

```text
MCP + escrita controlada + Android voice + Calendar/Tasks + Alexa
```

O maior cuidado arquitetural é manter separação clara entre:

```text
memória humana
memória técnica
índice RAG
ações operacionais
contextos de usuários
```

Com essas bases, a Alba pode se tornar uma assistente pessoal/familiar de contexto, capaz de lembrar, organizar, consultar e ajudar a executar ideias sem virar um sistema excessivamente complexo desde o início.

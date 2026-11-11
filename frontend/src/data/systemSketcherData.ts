export const SYSTEM_SKETCHER_MARKDOWN = `# SystemSketcher — Product Reverse Engineering & Technical Analysis

**Research and Technical Discovery Report**

**Website:** https://www.systemsketcher.com/  
**Related Tool:** REA — Reverse Engineer Anything  
**REA Setup Command:** \`npx rea-agents@latest setup\`  
**Report Date:** 11 November 2026

---

## 1. Executive Summary

SystemSketcher is a browser-based system architecture diagramming product designed to help developers and software architects visually design, communicate, and refine software infrastructure.

Its central value proposition combines three capabilities:

1. A visual diagramming canvas for designing system architectures.
2. A reusable component library containing more than 830 advertised components.
3. AI-assisted architecture suggestions and diagram creation.

The product aims to simplify the process of translating an abstract software architecture into a visual representation.

The public website advertises:
- Visual system architecture editing.
- A large component library.
- Drag-and-drop diagram construction.
- AI-powered suggestions.
- Sample architecture diagrams.
- PNG and JSON export.
- Access without mandatory sign-up.

This report separates publicly advertised functionality from proposed technical architecture. The exact production implementation, internal source code, API endpoints, and backend infrastructure have not been verified.

## 2. Product Overview

### 2.1 What is SystemSketcher?

SystemSketcher is a visual system design environment.

It enables users to represent how different parts of an application communicate with one another.

For example, a typical web application might contain:

- Frontend application.
- API gateway.
- Backend services.
- Authentication service.
- Database.
- Cache.
- Message queue.
- Cloud storage.
- Monitoring infrastructure.

Instead of explaining all these components through text, users can arrange them on a canvas and connect them through visual relationships.

### 2.2 Target Audience

The likely target audience includes:

- Software architects.
- Backend developers.
- Full-stack developers.
- Cloud engineers.
- DevOps engineers.
- Engineering students.
- System design interview candidates.
- Technical founders and product teams.

### 2.3 Main Product Value

The product reduces the effort required to create and communicate architecture diagrams.

Its AI capabilities potentially reduce the need to manually construct every component and connection.

---

## 3. Main Features and Functionalities

### 3.1 Visual Architecture Canvas

The canvas is the primary workspace.

Expected capabilities to investigate include:

- Component placement.
- Drag-and-drop interactions.
- Node selection.
- Component movement.
- Connection creation.
- Diagram arrangement.
- Zooming and panning.
- Component deletion.
- Diagram editing.
- Undo and redo.

The exact availability of each interaction must be confirmed through hands-on browser inspection.

### 3.2 Component Library

The website advertises a catalog of more than 830 components.

The catalog is a significant part of the product because it allows users to build diagrams using recognizable infrastructure symbols.

Potential component categories include:

**Cloud infrastructure**
- AWS services.
- Compute resources.
- Serverless functions.
- Load balancers.
- API gateways.
- Networking services.
- Cloud storage.

**Databases and storage**
- PostgreSQL.
- MySQL.
- MongoDB.
- Redis.
- Object storage.
- Search indexes.
- Distributed databases.

**Application components**
- Web applications.
- Mobile applications.
- Backend services.
- Authentication services.
- External APIs.
- Microservices.

**Messaging and event processing**
- Message queues.
- Event brokers.
- Kafka-style streaming.
- Event consumers.
- Notification services.

**DevOps and monitoring**
- Docker.
- Kubernetes.
- CI/CD.
- Logging.
- Metrics.
- Monitoring systems.

These are representative categories for technical classification, not a verified complete catalog of SystemSketcher.

### 3.3 Connections and Relationships

Connections describe how components communicate.

Examples include:

- Frontend to API gateway.
- API gateway to backend service.
- Backend service to database.
- Application to cache.
- Producer to message queue.
- Storage to processing service.

A robust connection model should support:

- Source component.
- Destination component.
- Connection direction.
- Optional labels.
- Connection styling.
- Routing information.

### 3.4 AI-Assisted Architecture Design

AI is one of the main differentiators of the product.

The publicly advertised AI functionality includes architecture suggestions.

The broader capabilities worth investigating include:

- Natural-language architecture generation.
- Architecture improvement suggestions.
- Diagram generation.
- Section-based editing.
- Sketch-to-diagram workflows.
- Architecture recommendations.

The latter capabilities require direct interaction testing before they can be considered verified product features.

### 3.5 Export Functionality

The public website advertises:

**PNG export**
- Creates a visual image of the architecture.
- Useful for presentations and documentation.

**JSON export**
- Preserves a structured representation.
- Useful for diagram restoration, processing, and integration with other tools.

JSON export is particularly important because it means a diagram can potentially be treated as editable application data rather than only as an image.

### 3.6 Sample Architectures

The website advertises sample architecture designs, including:

**E-commerce architecture**
- Product catalog.
- Order management.
- Payment processing.
- Inventory.
- Database.
- Cache.

**URL shortener architecture**
- URL input.
- Hash generation.
- Mapping storage.
- Redirection service.
- Database.

**Video streaming architecture**
- Video upload.
- Processing and transcoding.
- Content storage.
- CDN delivery.
- Metadata database.

These examples demonstrate how the tool can be used to communicate real-world system designs.

---

## 4. Product Architecture — Proposed Technical Model

The following architecture represents a reasonable implementation model for a product like SystemSketcher. It is not a confirmed representation of its production infrastructure.

### 4.1 Frontend Layer

Responsibilities:

- User interface.
- Architecture canvas.
- Component sidebar.
- Toolbar.
- Properties panel.
- Diagram interaction.
- Export controls.

Recommended technology:
- React.
- TypeScript.
- SVG or Canvas rendering.
- A graph editor library.

### 4.2 Diagram State Management

The application should maintain structured diagram state.

Core objects:

**Nodes**
- ID.
- Component type.
- Display name.
- Position.
- Dimensions.
- Icon.
- Properties.

**Edges**
- ID.
- Source node.
- Destination node.
- Direction.
- Label.
- Styling.

**Diagram metadata**
- Diagram ID.
- Name.
- Version.
- Created date.
- Updated date.
- Viewport settings.

### 4.3 Component Registry

A component registry maintains the available architecture components.

Each component should contain:

- Unique identifier.
- Component name.
- Category.
- Icon.
- Description.
- Default properties.
- Vendor.
- Optional documentation reference.

This registry makes it easier to support hundreds or thousands of reusable elements.

### 4.4 AI Orchestration Layer

The AI system should convert natural-language requirements into structured diagram modifications.

Example:

User instruction:

"Create an e-commerce architecture using AWS, Redis, PostgreSQL, and an API gateway."

Expected processing:

1. Interpret the requirements.
2. Identify appropriate component types.
3. Generate node definitions.
4. Generate connection definitions.
5. Arrange the diagram.
6. Validate the resulting graph.
7. Return structured JSON.
8. Render the architecture on the canvas.

An important design principle is that AI should generate structured diagram operations, not simply return an image.

### 4.5 Persistence Layer

A possible backend could store:

- User profiles.
- Saved diagrams.
- Component metadata.
- Templates.
- Diagram versions.
- User preferences.

Whether SystemSketcher uses persistent cloud storage for all these entities requires further investigation.

### 4.6 Export Engine

The export engine should support:

- PNG rendering.
- JSON serialization.
- JSON deserialization.
- Diagram restoration.
- Optional SVG output.

---

## 5. Example Diagram Data Structure

The following is an illustrative schema for a SystemSketcher-like application.

\`\`\`json
{
  "version": 1,
  "diagram": {
    "name": "E-commerce Architecture"
  },
  "nodes": [
    {
      "id": "frontend",
      "type": "application",
      "label": "Frontend",
      "x": 100,
      "y": 100
    },
    {
      "id": "api",
      "type": "api_gateway",
      "label": "API Gateway",
      "x": 350,
      "y": 100
    },
    {
      "id": "database",
      "type": "database",
      "label": "PostgreSQL",
      "x": 600,
      "y": 100
    }
  ],
  "edges": [
    {
      "id": "connection-1",
      "source": "frontend",
      "target": "api"
    },
    {
      "id": "connection-2",
      "source": "api",
      "target": "database"
    }
  ]
}
\`\`\`

This is a proposed data structure and not the actual SystemSketcher JSON export format.

---

## 6. REA — Reverse Engineer Anything

### 6.1 What is REA?

REA stands for Reverse Engineer Anything.

It is a toolkit designed to help coding agents investigate software systems through structured analysis workflows.

It can be used for suitable reverse-engineering tasks involving:

- Websites.
- JavaScript applications.
- Software projects.
- Application bundles.
- Native binaries, where supported.
- Application behavior and architecture.

REA is useful because it gives an agent a more structured investigation process instead of relying only on manually reading code.

### 6.2 Installation Command

\`\`\`bash
npx rea-agents@latest setup
\`\`\`

### 6.3 Proposed Setup Process

1. Check Node.js and npm.
2. Select a supported coding agent.
3. Run the REA setup command.
4. Review proposed configuration changes.
5. Approve the setup.
6. Restart the coding agent.
7. Run diagnostics.
8. Verify MCP connectivity.
9. Verify that REA tools are available to the agent.

### 6.4 Installation Verification

For Codex, the documented diagnostic command is:

\`\`\`bash
npx -y rea-agents@latest doctor --client codex --json
\`\`\`

Expected health indicator:

\`\`\`json
{
  "healthy": true
}
\`\`\`

The exact diagnostic output may contain additional fields.

### 6.5 Important Setup Limitation

The installation requires execution in a supported local development environment.

A browser-based ChatGPT conversation does not automatically provide access to the user's local terminal.

Therefore, the installation must be performed and verified in the selected coding agent's environment.

**Current status: Setup plan prepared; installation and local verification pending.**

---

## 7. Reverse-Engineering Methodology for SystemSketcher

A complete technical investigation should be divided into five phases.

### Phase 1: Public Website Analysis

Investigate:

- Homepage.
- Product description.
- Navigation.
- Sample architectures.
- Advertised features.
- Export options.
- Public documentation.
- Pricing and access model, if published.

Deliverable: Product specification.

### Phase 2: Browser Interaction Analysis

Open the application in Chrome, Chromium, or Edge.

Inspect:

- Main canvas.
- Component sidebar.
- Toolbar.
- Search.
- Dialogs.
- Menus.
- Properties panels.
- Drag-and-drop behavior.
- Keyboard shortcuts.
- AI interactions.
- Export workflows.

Deliverable: UI component inventory and interaction map.

### Phase 3: Network Investigation

Observe application requests during:

- Initial page load.
- Canvas initialization.
- Component search.
- Diagram generation.
- AI requests.
- Saving.
- Exporting.

Identify:

- API endpoints.
- Request formats.
- Response structures.
- Authentication requirements.
- External service dependencies.
- Client-side versus server-side operations.

Deliverable: Network and API behavior report.

### Phase 4: Frontend Asset Analysis

Investigate publicly accessible frontend assets.

Inspect:

- JavaScript bundles.
- CSS assets.
- Component definitions.
- Dependencies.
- Icon resources.
- Application state.
- Data serialization.
- Routing.

Deliverable: Frontend technology and component architecture report.

### Phase 5: Technical Reconstruction

Combine the findings into:

- Product requirements document.
- System architecture diagram.
- UI component hierarchy.
- Interaction specification.
- Data model.
- API map.
- AI workflow specification.
- Implementation roadmap.

Deliverable: Full technical reconstruction document.

---

## 8. Recommended Technology Stack for Building a Similar Product

The following is a proposed stack, not a statement of SystemSketcher's actual stack.

| Layer | Recommended technology |
|---|---|
| Frontend | React |
| Language | TypeScript |
| UI | Tailwind CSS |
| Diagram editor | React Flow / XYFlow |
| Rendering | SVG and Canvas |
| State management | Zustand |
| Backend | Node.js / Python |
| API | REST |
| AI orchestration | LLM API with structured outputs |
| Database | PostgreSQL |
| Cache | Redis |
| File storage | S3-compatible object storage |
| Export | SVG-to-PNG rendering |
| Validation | Zod |
| Deployment | Vercel / cloud infrastructure |

### Suggested development priorities

**Stage 1 — Core editor**
- Canvas.
- Drag-and-drop.
- Nodes and edges.
- Selection.
- Zoom and pan.
- Undo and redo.

**Stage 2 — Component library**
- Search.
- Categories.
- Vendor icons.
- Custom components.
- Component properties.

**Stage 3 — Diagram engine**
- JSON schema.
- Import and export.
- Validation.
- Auto-layout.
- Diagram restoration.

**Stage 4 — AI integration**
- Natural-language generation.
- AI-assisted editing.
- Architecture suggestions.
- Structured diagram modifications.
- Validation.

**Stage 5 — Product features**
- PNG export.
- Templates.
- Saving.
- Sharing.
- User accounts, if needed.

---

## 9. Final Assessment

SystemSketcher's product concept is built around a straightforward but valuable idea: make software architecture design visual, accessible, reusable, and AI-assisted.

Its most important product assets are:

1. The interactive architecture editor.
2. The extensive component library.
3. The underlying diagram data model.
4. AI-assisted diagram generation and refinement.
5. Reusable architecture templates.
6. Export and integration capabilities.

For someone looking to develop a similar product, the diagram engine and component library are the foundational investments. AI should be built on top of a reliable structured diagram model rather than used as a substitute for one.

### Research confidence

| Area | Confidence |
|---|---|
| Product purpose | High |
| Publicly advertised features | High |
| Sample architectures | High |
| Complete component inventory | Not verified |
| Exact frontend framework | Not verified |
| Actual backend architecture | Not verified |
| Actual API endpoints | Not verified |
| Internal AI implementation | Not verified |
| REA local installation | Pending |

---

## 10. Next Steps

The recommended next actions are:

- [ ] Select the coding agent for REA.
- [ ] Confirm the operating system.
- [ ] Run \`npx rea-agents@latest setup\`.
- [ ] Review and approve the setup changes.
- [ ] Run REA diagnostics.
- [ ] Connect the browser investigation workflow.
- [ ] Inspect SystemSketcher's live application.
- [ ] Extract the complete accessible component inventory.
- [ ] Investigate AI generation and editing behavior.
- [ ] Reconstruct the diagram data model.
- [ ] Produce a verified technical architecture report.

**Final objective:** Move from a high-level understanding of SystemSketcher to an evidence-backed technical specification that can guide the development of a comparable system architecture design platform.

**Important:** This document is an initial public-product analysis and proposed technical reconstruction. It is not a completed source-code reverse engineering report or proof of REA installation.
`

export const SYSTEM_SKETCHER_METADATA = {
  title: 'SystemSketcher — Product Reverse Engineering & Technical Analysis',
  subtitle: 'Research and Technical Discovery Report',
  website: 'https://www.systemsketcher.com/',
  relatedTool: 'REA — Reverse Engineer Anything',
  setupCommand: 'npx rea-agents@latest setup',
  doctorCommand: 'npx -y rea-agents@latest doctor --client codex --json',
  reportDate: '11 November 2026',
}

export const EXAMPLE_DIAGRAM_JSON = {
  version: 1,
  diagram: {
    name: 'E-commerce Architecture',
  },
  nodes: [
    {
      id: 'frontend',
      type: 'application',
      label: 'Frontend',
      x: 100,
      y: 100,
    },
    {
      id: 'api',
      type: 'api_gateway',
      label: 'API Gateway',
      x: 350,
      y: 100,
    },
    {
      id: 'database',
      type: 'database',
      label: 'PostgreSQL',
      x: 600,
      y: 100,
    },
  ],
  edges: [
    {
      id: 'connection-1',
      source: 'frontend',
      target: 'api',
    },
    {
      id: 'connection-2',
      source: 'api',
      target: 'database',
    },
  ],
}

export const TECH_STACK_TABLE = [
  { layer: 'Frontend', tech: 'React' },
  { layer: 'Language', tech: 'TypeScript' },
  { layer: 'UI', tech: 'Tailwind CSS' },
  { layer: 'Diagram editor', tech: 'React Flow / XYFlow' },
  { layer: 'Rendering', tech: 'SVG and Canvas' },
  { layer: 'State management', tech: 'Zustand' },
  { layer: 'Backend', tech: 'Node.js / Python' },
  { layer: 'API', tech: 'REST' },
  { layer: 'AI orchestration', tech: 'LLM API with structured outputs' },
  { layer: 'Database', tech: 'PostgreSQL' },
  { layer: 'Cache', tech: 'Redis' },
  { layer: 'File storage', tech: 'S3-compatible object storage' },
  { layer: 'Export', tech: 'SVG-to-PNG rendering' },
  { layer: 'Validation', tech: 'Zod' },
  { layer: 'Deployment', tech: 'Vercel / cloud infrastructure' },
]

export const RESEARCH_CONFIDENCE_TABLE = [
  { area: 'Product purpose', confidence: 'High' },
  { area: 'Publicly advertised features', confidence: 'High' },
  { area: 'Sample architectures', confidence: 'High' },
  { area: 'Complete component inventory', confidence: 'Not verified' },
  { area: 'Exact frontend framework', confidence: 'Not verified' },
  { area: 'Actual backend architecture', confidence: 'Not verified' },
  { area: 'Actual API endpoints', confidence: 'Not verified' },
  { area: 'Internal AI implementation', confidence: 'Not verified' },
  { area: 'REA local installation', confidence: 'Pending' },
]

export const NEXT_STEPS_CHECKLIST = [
  'Select the coding agent for REA.',
  'Confirm the operating system.',
  'Run npx rea-agents@latest setup.',
  'Review and approve the setup changes.',
  'Run REA diagnostics.',
  'Connect the browser investigation workflow.',
  'Inspect SystemSketcher\'s live application.',
  'Extract the complete accessible component inventory.',
  'Investigate AI generation and editing behavior.',
  'Reconstruct the diagram data model.',
  'Produce a verified technical architecture report.',
]


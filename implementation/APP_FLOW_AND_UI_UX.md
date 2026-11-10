# App Flow and UI/UX

## Primary flow
1. New project: user describes the app in one or two sentences (for example, a dating app with profiles, matching, image uploads, and real-time chat).
2. Requirements interview: ask one question at a time about concurrent users, geography, message volume, privacy/compliance, availability, and budget. Allow skipping with explicitly marked assumptions.
3. Requirements review: user edits and confirms a summary.
4. Retrieval and planning: show progress for retrieval, planning, and validation; stream partial results.
5. Whiteboard canvas: display the proposal on the infinite canvas with validation status.
6. Inspect: component panel shows purpose, rationale, citations, assumptions, alternatives, cost units, and failure modes.
7. Edit: drag components from the palette, draw shapes/text/freehand annotations, add/remove/replace components (smart drop-downs suggest only catalog-compatible components), edit connections, or change requirements.
8. Re-plan and validate affected areas; show a diff.
9. Update capacity and cost estimates.
10. Export PNG, SVG, Markdown, Mermaid, or JSON (PDF post-MVP).

## Secondary flows
- Knowledge administration: upload documents, choose collection, set licence/date, ingest, inspect status and chunk previews.
- Catalog administration: edit components, compatibility rules, limits, and cost units.
- Evaluation: run the evaluation set and compare results.

## Errors and edge states
- Invalid planner JSON: retry at most twice, then show a friendly error without raw reasoning.
- Validator issues: show inline on canvas with a one-click AI fix action.
- No relevant evidence: label proposal low-evidence and identify assumptions.
- LLM server offline: show service status and retry action.

## Screen map
Top bar: Overview, Whiteboard Templates, Compatibility Engine, Catalog, Projects, Knowledge, Settings. Project flow: Projects → Interview → Requirements review → Canvas. Canvas side panels: Component, Validation, Evidence, Cost, AI tools.

## Layout and interaction
Reference: SystemSketcher canvas (https://www.systemsketcher.com/canvas).
- Top bar (app navigation): brand, Overview, Whiteboard Templates, Compatibility Engine, Catalog, Projects, theme toggle.
- Canvas header: project name, validation badge, re-plan, export.
- Left component palette around 240px (collapsible): search plus collapsible categories from the catalog; drag onto the canvas.
- Center: infinite React Flow canvas (pan/zoom without bounds) with grid toggle, minimap, and zoom controls.
- Floating canvas toolbar: select/pan, rectangle, ellipse, arrow, elbow connector, text, freehand, bring forward/back, lock, undo/redo, delete, eraser, templates library, export.
- Right-click context menu: duplicate, replace, delete, lock, explain with AI.
- Right panel around 360px with Component, Validation, Evidence, Cost, and AI tools tabs (Generate from description, Refine selection, Score design).
- Bottom drawer: architect chat and requirement chips.
- Canvas layers: Clients, Edge, Services, Data stores, Async, Observability.
- Nodes use layer colors and validation borders; edges show HTTPS, WebSocket, or async protocol labels.
- Reject invalid connections with a tooltip describing the compatibility rule.
- Highlight changed nodes after re-planning and show a diff.
- Whiteboard templates (e.g. e-commerce, real-time streaming, AI/RAG) load onto the canvas in one click.

## Key components
- RequirementChip: editable value with an assumed badge when defaulted.
- EvidenceCard: title, collection, date, snippet, and relevance score.
- ValidationIssueRow: severity, affected node, message, and Fix with AI action.
- ComponentPanel: purpose, rationale, alternatives, failure modes, and cost units.
- CostTable: line items, units, quantity assumptions, and monthly estimate range.

## Visual and accessibility principles
- Calm, technical developer-tool interface; evidence is visible and the canvas is primary.
- Dark and light themes with a top-bar toggle, defaulting to system. Use neutral greys, one accent, and semantic green/amber/red.
- Use an 8px spacing grid, restrained borders, and 8–12px radii.
- Keyboard navigation and visible focus rings throughout, including the canvas.
- Never rely on color alone for validation; pair color with icons and labels.
- Desktop-first; tablet right panel becomes a drawer; mobile is read-only.
- Empty canvas offers example prompts; loading shows progress steps; errors explain cause and next action.

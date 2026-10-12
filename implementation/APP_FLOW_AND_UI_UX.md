# App Flow and UI/UX

## Primary flow
1. New project: user describes the app in one or two sentences (for example, a dating app with profiles, matching, image uploads, and real-time chat).
2. Requirements interview: ask one question at a time about concurrent users, geography, message volume, privacy/compliance, availability, and budget. Allow skipping with explicitly marked assumptions.
3. Requirements review: user edits and confirms a summary.
4. Retrieval and planning: show progress for retrieval, planning, and validation; stream partial results.
5. Architecture canvas: display the proposal and validation status.
6. Inspect: component panel shows purpose, rationale, citations, assumptions, alternatives, cost units, and failure modes.
7. Edit: add/remove/replace components, edit connections, or change requirements.
8. Re-plan and validate affected areas; show a diff.
9. Update capacity and cost estimates.
10. Export Markdown, PDF, Mermaid, or JSON.

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
Home → Project list → Interview → Requirements review → Canvas. Canvas side panels: Component, Validation, Evidence, Cost. Settings and Knowledge/Catalog administration live in the sidebar.

## Layout and interaction
- Left sidebar around 240px: projects, knowledge base, catalog, evaluations, settings.
- Center: React Flow canvas with minimap and zoom controls.
- Right panel around 360px with Component, Validation, Evidence, and Cost tabs.
- Bottom drawer: architect chat and requirement chips.
- Top bar: project name, validation badge, re-plan, export.
- Canvas layers: Clients, Edge, Services, Data stores, Async, Observability.
- Nodes use layer colors and validation borders; edges show HTTPS, WebSocket, or async protocol labels.
- Reject invalid connections with a tooltip describing the compatibility rule.
- Highlight changed nodes after re-planning and show a diff.

## Key components
- RequirementChip: editable value with an assumed badge when defaulted.
- EvidenceCard: title, collection, date, snippet, and relevance score.
- ValidationIssueRow: severity, affected node, message, and Fix with AI action.
- ComponentPanel: purpose, rationale, alternatives, failure modes, and cost units.
- CostTable: line items, units, quantity assumptions, and monthly estimate range.

## Visual and accessibility principles
- Calm, technical developer-tool interface; evidence is visible and the canvas is primary.
- Dark and light themes, defaulting to system. Use neutral greys, one accent, and semantic green/amber/red.
- Use an 8px spacing grid, restrained borders, and 8–12px radii.
- Keyboard navigation and visible focus rings throughout, including the canvas.
- Never rely on color alone for validation; pair color with icons and labels.
- Desktop-first; tablet right panel becomes a drawer; mobile is read-only.
- Empty canvas offers example prompts; loading shows progress steps; errors explain cause and next action.

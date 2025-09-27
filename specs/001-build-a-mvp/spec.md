# Feature Specification: MVP Flask Server with Celery Crawler

**Feature Branch**: `[001-build-a-mvp]`  
**Created**: 2025-09-27  
**Status**: Draft  
**Input**: User description: "build a mvp flask server, that integrate with celery, that allow to trigger crawl comic and novel from multiple site, that can store metadata in postgres and image or text in folder, using beautiysoup"

## Execution Flow (main)
```
1. Parse user description from Input
   → If empty: ERROR "No feature description provided"
2. Extract key concepts from description
   → Identify: actors, actions, data, constraints
3. For each unclear aspect:
   → Mark with [NEEDS CLARIFICATION: specific question]
4. Fill User Scenarios & Testing section
   → If no clear user flow: ERROR "Cannot determine user scenarios"
5. Generate Functional Requirements
   → Each requirement must be testable
   → Mark ambiguous requirements
6. Identify Key Entities (if data involved)
7. Run Review Checklist
   → If any [NEEDS CLARIFICATION]: WARN "Spec has uncertainties"
   → If implementation details found: ERROR "Remove tech details"
8. Return: SUCCESS (spec ready for planning)
```

---

## ⚡ Quick Guidelines
- ✅ Focus on WHAT users need and WHY
- ❌ Avoid HOW to implement (no tech stack, APIs, code structure)
- 👥 Written for business stakeholders, not developers

### Section Requirements
- **Mandatory sections**: Must be completed for every feature
- **Optional sections**: Include only when relevant to the feature
- When a section doesn't apply, remove it entirely (don't leave as "N/A")

### For AI Generation
- Mark all ambiguities: Use [NEEDS CLARIFICATION: specific question] for any assumption you'd need to make
- Don't guess: If the prompt doesn't specify something (e.g., "login system" without auth method), mark it
- Think like a tester: Every vague requirement should fail the "testable and unambiguous" checklist item
- Common underspecified areas:
   - User types and permissions
   - Data retention/deletion policies  
   - Performance targets and scale
   - Error handling behaviors
   - Integration requirements
   - Security/compliance needs

---

## User Scenarios & Testing

### Primary User Story
A user triggers a crawl for comics or novels from a supported site. The system fetches metadata and content, stores metadata in Postgres, and saves images or text in a folder. The user can check crawl status and results.

### Acceptance Scenarios
- User can trigger a crawl for a specific comic or novel from a supported site
- System fetches and stores metadata in Postgres
- System saves images (for comics) or text (for novels) in a folder
- User can check crawl status and see results
- Supported sites are loaded from a config file
- System supports both manual and scheduled crawling
- System logs errors, shows errors in UI, retries failed crawls, and allows manual retrigger of failed crawls
- Basic authentication is required for access
- System supports high concurrency and large scale

## Functional Requirements
- The system MUST allow users to trigger a crawl for comics or novels from multiple sites
- The system MUST store metadata in Postgres
- The system MUST store images or text in a folder
- The system MUST provide crawl status and results to the user
- The system MUST use Celery for background crawling tasks
- The system MUST use BeautifulSoup for parsing site content
- Supported sites MUST be loaded from a config file
- The system MUST support both manual and scheduled crawling
- The system MUST log errors, show errors in UI, retry failed crawls, and allow manual retrigger of failed crawls
- The system MUST require basic authentication for access
- The system MUST support high concurrency and large scale
- The system MUST support crawling https://nettruyen3qb.com/ as an initial site
- The system MUST allow configuration of maximum RAM usage to control concurrent crawls
- [NEEDS CLARIFICATION: Required metadata fields]

## Key Entities
- Comic (id, title, author, site, metadata, image folder path)
- Novel (id, title, author, site, metadata, text folder path)
- CrawlTask (id, type, status, site, target, result, error)

---

## Review Checklist
- [ ] All user scenarios are covered
- [ ] All requirements are testable
- [ ] All ambiguities are marked with [NEEDS CLARIFICATION]
- [ ] No implementation details included
- [ ] Key entities identified

## Clarifications
### Session 2025-09-27
- Q: How are supported sites configured or extended? → A: Loaded from a config file
- Q: What is the expected crawl frequency or scheduling? → A: Both manual and scheduled
- Q: What error handling/reporting is required for failed crawls? → A: Log, UI, retry, manual retrigger
- Q: Are there user roles or permissions? → A: Basic authentication required
- Q: What are the performance/scale expectations? → A: High concurrency, large scale
- Q: List of initial supported sites? → A: https://nettruyen3qb.com/
- Q: Maximum concurrent crawls? → A: Can configure the max RAM usage
- [ ] Pending answers to clarification questions above

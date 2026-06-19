# Website Build Brief — Energy Label Website

## Goal

Create a clean, simple, neutral HTML landing page for an energy label advisory service in the Netherlands.

The website should focus primarily on **individual expats and international clients living in the Netherlands** who are buying or selling their home.

A secondary audience is **international investors** interested in Dutch real estate portfolios.

The output should be a single responsive HTML file with embedded CSS.

---

## Design Direction

Use a simple, clean, neutral visual style inspired by modern consultancy websites.

### Visual Style

- White background
- Soft grey sections
- Muted blue accent color
- Lots of whitespace
- Rounded cards
- Clear hierarchy
- Professional but friendly
- No clutter
- No heavy animations

### Tone

- Clear
- Trustworthy
- International
- Practical
- Non-technical
- Easy to understand

---

## Navigation

Top navigation should include:

1. Price
2. Process
3. Investors
4. Contact

Layout:

```text
LOGO                          Price | Process | Investors | Contact
```

The logo can be simple placeholder text for now.

Suggested logo placeholder:

```text
Energy Label NL
```

---

## Homepage Structure

The homepage should contain the following sections:

1. Header / Navigation
2. Split Hero Section
3. Trust Bar
4. Process Section
5. Pricing Section
6. Why Choose Us Section
7. Contact Section

---

## 1. Header / Navigation

Create a clean top bar.

### Requirements

- Logo on the left
- Navigation links on the right
- Sticky header optional
- White background
- Thin bottom border
- Mobile responsive

### Navigation Labels

- Price
- Process
- Investors
- Contact

---

## 2. Split Hero Section

Create a split hero section with two audience blocks.

The left block should be dominant and focus on expats.
The right block should be smaller and focus on investors.

### Layout Ratio

- Expats block: approximately 70%
- Investors block: approximately 30%

On mobile, stack the two blocks vertically.

---

### Left Hero Block — Expats

This is the primary audience.

#### Label

```text
For expats and internationals
```

#### Headline

```text
Buying or selling a home in the Netherlands?
```

#### Supporting Text

```text
Get your energy label fast and actually understand what it means.
```

#### Buttons

Primary button:

```text
Get Energy Label
```

Secondary button:

```text
See Prices
```

---

### Right Hero Block — Investors

This is secondary and should be visually quieter.

#### Label

```text
For international investors
```

#### Headline

```text
Investing in Dutch real estate?
```

#### Supporting Text

```text
Portfolio scans and ROI-driven upgrade advice for residential properties.
```

#### Button

```text
For Investors →
```

---

## 3. Trust Bar

Create a small trust bar directly below the hero.

Do not overstate traction because the business is new.

### Trust Bar Items

```text
🇬🇧 English-speaking support
🇨🇳 中文服务
Certified energy label specialist
```

### Style

- Light grey background
- Small icons / flags
- Horizontal layout on desktop
- Stack or wrap on mobile

---

## 4. Process Section

Section ID:

```text
process
```

### Section Title

```text
How it works
```

### Subtitle

```text
A simple process from intake to registered energy label.
```

### Three Steps

#### Step 1

Title:

```text
Upload details
```

Text:

```text
Share your property details and available documents.
```

#### Step 2

Title:

```text
We assess
```

Text:

```text
We review the property information and prepare the energy label assessment.
```

#### Step 3

Title:

```text
You receive results
```

Text:

```text
You receive the registered energy label with a clear explanation in English or Chinese.
```

### Layout

Use three cards in a row on desktop.
Stack vertically on mobile.

---

## 5. Pricing Section

Section ID:

```text
price
```

### Section Title

```text
Clear pricing — based on your property type
```

### Subtitle

```text
No hidden costs. Delivered within 5 working days.
```

---

## Pricing Visual

Create two main pricing cards:

1. Apartment
2. Single Family Home

Use icons or simple visual symbols.

---

### Pricing Card 1 — Apartment

#### Title

```text
Apartment
```

#### Description

```text
For apartments, flats, and studios.
```

#### Price

```text
€XXX
```

#### Includes

- Official energy label
- Registration
- Basic explanation

#### Button

```text
Start now
```

---

### Pricing Card 2 — Single Family Home

#### Title

```text
Single Family Home
```

#### Description

```text
For row houses, corner houses, and detached houses.
```

#### Price Table Inside Card

Create a small internal table:

| Property type | Price | Note |
|---|---:|---|
| Row house | €XXX | Most common |
| Corner house | €XXX | Larger surface |
| Detached house | €XXX* | Up to 300 m² |

#### Includes

- Official energy label
- Registration
- Full assessment
- Basic explanation

#### Button

```text
Get started
```

---

### Pricing Footnote

Below the pricing cards, include:

```text
*Detached house pricing applies up to 300 m². Larger properties are quoted based on size and complexity.
```

### Language Explanation Line

Below the footnote, include:

```text
Your energy label, clearly explained in English or Chinese.
```

---

## 6. Why Choose Us Section

Section Title:

```text
Why choose us?
```

### Three Benefits

#### Benefit 1

Title:

```text
No Dutch jargon
```

Text:

```text
We explain the Dutch energy label process in clear language.
```

#### Benefit 2

Title:

```text
Built for internationals
```

Text:

```text
Support available in English and Chinese.
```

#### Benefit 3

Title:

```text
Clear process
```

Text:

```text
You know what to expect before the assessment starts.
```

---

## 7. Contact Section

Section ID:

```text
contact
```

### Title

```text
Ready to get your energy label?
```

### Subtitle

```text
Send your property details and we will get back to you with the next step.
```

### Form Fields

- Name
- Email
- Phone number
- Property type
- Message

### Property Type Dropdown Options

- Apartment
- Row house
- Corner house
- Detached house
- Larger property / portfolio

### Buttons

Primary:

```text
Submit request
```

Secondary:

```text
Contact via WhatsApp
```

---

## Investor Section / Link Behavior

The investor block in the hero should link to a later section or separate page.

For now, create a short investor section after the main expat-focused content or as a preview block.

### Investor Preview Title

```text
For international property investors
```

### Investor Preview Text

```text
Planning to buy or upgrade multiple residential properties in the Netherlands? We support international investors with portfolio energy scans, technical due diligence, and ROI-driven improvement advice.
```

### Investor Services

- Portfolio energy and compliance scan
- Technical due diligence
- Upgrade roadmap
- ROI-driven improvement advice

### Investor CTA

```text
Request investor consultation
```

---

## Responsive Requirements

The HTML should be responsive.

### Desktop

- Header navigation in one row
- Hero split 70 / 30
- Pricing cards side by side
- Process cards in three columns

### Mobile

- Header navigation can wrap or become stacked
- Hero blocks stacked vertically
- Pricing cards stacked vertically
- Process cards stacked vertically
- Buttons full width if needed

---

## Suggested CSS Variables

Use CSS variables for easy editing.

```css
:root {
  --color-bg: #ffffff;
  --color-bg-soft: #f6f7f8;
  --color-text: #1f2933;
  --color-muted: #6b7280;
  --color-border: #e5e7eb;
  --color-accent: #2f6f8f;
  --color-accent-dark: #24566f;
  --radius-card: 18px;
  --shadow-soft: 0 10px 30px rgba(0, 0, 0, 0.06);
}
```

---

## Content Hierarchy

Use strong headings and short text.

Avoid long paragraphs.

Make it easy to scan.

---

## Important Content Rules

- Do not claim “500+ clients” or similar large numbers.
- Do not overstate experience.
- Do not use exaggerated marketing language.
- Do not promise 48-hour delivery.
- Use “Delivered within 5 working days.”
- Include English and Chinese support.
- Keep the website expat-first.
- Keep investor messaging secondary.

---

## Final Output Required

Create a single file:

```text
index.html
```

The file should include:

- HTML
- Embedded CSS
- Responsive layout
- Placeholder pricing with €XXX
- Placeholder contact form
- No external dependencies required
- Clean semantic structure

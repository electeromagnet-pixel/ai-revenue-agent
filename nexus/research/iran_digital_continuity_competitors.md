# Competitor landscape: offline continuity for small online sellers

Research date: 2026-11-23  
Hypothesis: Iranian micro-sellers may need a lightweight way to record orders and track fulfillment when their usual online channel is unavailable.

## Executive finding

The market is not empty. Sellers can already use hosted storefront builders, self-hosted commerce software, social-commerce workflows, messaging apps, spreadsheets, paper ledgers, or a human assistant. A generic order-management app would have weak differentiation.

The narrow question worth testing is whether a very small, mobile-first, local-only order ledger is valuable to sellers who currently take orders through social channels and need to keep operating when a cloud service or international platform is unreachable.

This is a research hypothesis, not a claim that the listed competitors fail during outages. Public feature pages reviewed here do not establish the exact offline behavior of every product.

## Alternatives and competitor map

| Alternative | What public evidence supports | Implication for NEXUS | What remains unverified |
|---|---|---|---|
| Sazito (Iranian hosted store builder) | Public product updates describe order editing, inventory adjustments after order changes, shipment tracking, order export, and mobile admin improvements. [Sazito updates](https://t.me/s/sazito) | Strong adjacent competitor for sellers who already operate a Sazito storefront. Do not rebuild ordinary order management without a sharper outage-specific use case. | Whether order entry/admin works fully offline; local data retention and recovery behavior; current plan limits. |
| Shopfa (Iranian hosted store builder) | Public updates describe mobile-friendly order management, order filters, Excel shipment-tracking imports, order status, and order retention controls. [Shopfa updates](https://t.me/s/ShopfaCom) | Adjacent competitor with established order workflows. | Whether any critical workflow remains usable without the hosted service or internet. |
| Portal and other Iranian store builders | A third-party comparison lists Portal among established Iranian store builders and describes order management, payment, shipping and marketing features. [Comparison](https://rankesh.com/shop-builder/) | Sellers who already pay for a store builder may not need a separate ledger unless it solves a distinct continuity problem. | Verify exact features, prices and offline behavior directly before making competitive claims. |
| WooCommerce | Official documentation describes order statuses, inventory management and manual confirmation for offline payment methods. [Order statuses](https://woocommerce.com/document/managing-orders/order-statuses/) [Inventory troubleshooting](https://woocommerce.com/document/managing-orders/troubleshooting-orders/) | Flexible alternative for merchants who own a website and can maintain WordPress hosting. | Standard web admin is not proof of offline-first order capture; offline POS generally requires a separate plugin/app and later sync. |
| Offline POS extensions for WooCommerce | Marketplace documentation describes third-party POS extensions with offline sale queues and later synchronization. [POS options](https://woocommerce.com/document/5-best-woocommerce-pos-plugins-for-connecting-online-and-physical-stores/) | Offline selling already exists in adjacent retail software. The opportunity cannot be described as the first offline order tool. | Compatibility, pricing, availability in Iran, payment integration, and suitability for Instagram-only micro-sellers. |
| Paper, spreadsheet, phone notes, local messaging apps, manual assistant | These are plausible substitutes, not yet measured in our interviews. Reporting on Iran's connectivity restrictions describes domestic apps and local services continuing in some conditions, while also noting limitations. [Bloomberg](https://www.bloomberg.com/features/2026-iran-internet) | These may be the true competitors for a very small seller. Ask what sellers actually use rather than assume a software gap. | Actual prevalence, workflow friction, backup practices, willingness to change, and willingness to pay. |

## Problem context

Reporting on Iran's 2026 internet disruptions describes online sellers losing access to storefronts, customers and income. [Washington Post](https://www.washingtonpost.com/business/2026/05/01/iran-us-war-internet-business-economy-online/) [Iran International](https://www.iranintl.com/en/202601295582) Bloomberg describes a domestic ecosystem of messaging and commerce alternatives, while noting that domestic network infrastructure has had failures of its own. [Bloomberg](https://www.bloomberg.com/features/2026-iran-internet)

These sources support investigating continuity. They do not prove that a separate application is wanted, safe, or commercially viable.

## Possible differentiation to test

1. Local-first capture: create and edit an order without network access after the page has been saved to the device.
2. No account required for the prototype: reduce setup friction; keep records on the seller's device.
3. Simple follow-up queue: show which orders need confirmation, packing, dispatch, or follow-up.
4. Portable records: export JSON and CSV so the seller is not locked in.
5. Honest boundary: no online messaging, payment processing, cloud backup, multi-device sync, or automatic reconciliation during a complete outage.

The prototype is a local demo. It is not a secure production system, does not encrypt local records, and should only be tested with dummy data until security and recovery are designed.

## Preliminary strategic conclusion

Do not build a full e-commerce platform. First test a small continuity layer for sellers who already sell through social channels and do not want to migrate their storefront.

A standalone product is justified only if interviews show a repeated, costly workflow gap that existing store builders, local tools, paper or spreadsheets do not already solve adequately.

## Open questions

- Which seller segment is affected most?
- What exactly stops when the internet is unreliable: receiving orders, reading old orders, checking stock, confirming payments, arranging delivery, or contacting customers?
- Do sellers already have a paper/Excel/local-app backup?
- Would a phone-only offline ledger fit their actual device and workflow?
- What information are they comfortable storing locally?
- Is the problem frequent and expensive enough to justify a paid tool?
- Would sellers pay, and what observable behavior supports that claim?

## Evidence quality

Product feature claims are based on vendor-published update channels where available; they are not independent product tests. The Portal comparison is a third-party review, not a vendor guarantee. News reporting documents connectivity and business impacts, not software demand. Offline capabilities are marked unverified unless cited documentation explicitly describes them.

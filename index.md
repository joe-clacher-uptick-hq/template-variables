---
title: Django Template Variables Documentation
layout: default
---

# Django Template Variables Documentation

## accreditation

<details class="expandable-section">
<summary><strong>Found in files</strong></summary>

- [AARHUSFIRE] - [templates] - [Service Report (Prompts)](https://AARHUSFIRE.onuptick.com/configuration/templates)
- [ABACUSFAS] - [emails] - [test](https://ABACUSFAS.onuptick.com/configuration/emails)

</details>

### Properties

| Property | Example Usage |
|----------|---------------|
| `name` | {{accreditation.name}} |
| `number` | {{ accreditation.number }} |

<details class="expandable-section">
<summary><strong>Usage Examples</strong></summary>

```django

<td>
{% for accreditation in technician.accreditations %}
<div>{{accreditation.name}}: {{ accreditation.number }}</div>
{% endfor %}
</td>

```

</details>

---

## after_photos

<details class="expandable-section">
<summary><strong>Found in files</strong></summary>

- [AARHUSFIRE] - [templates] - [Service Report (Prompts)](https://AARHUSFIRE.onuptick.com/configuration/templates)
- [ABACUSFAS] - [emails] - [test](https://ABACUSFAS.onuptick.com/configuration/emails)

</details>

<details class="expandable-section">
<summary><strong>Usage Examples</strong></summary>

```django

<strong>After</strong>
<div class="...">
{% for photo in after_photos %}
{% include "webtemplates/2022-photo-tile" with photo=photo class="..." %}
{% endfor %}

```

</details>

---

## appointments

<details class="expandable-section">
<summary><strong>Found in files</strong></summary>

- [AARHUSFIRE] - [emails] - [Appointment Scheduled Email](https://AARHUSFIRE.onuptick.com/configuration/emails)

</details>

### Properties

| Property | Example Usage |
|----------|---------------|
| `scheduled_start` | {{appointments.scheduled_start}} |
| `task` | {{appointments.task.property.name}} |
| `task.name` | {{appointments.task.name}} |
| `task.property` | {{appointments.task.property.name}} |
| `task.property.name` | {{appointments.task.property.name}} |

<details class="expandable-section">
<summary><strong>Usage Examples</strong></summary>

```django

{% timezone appt.timezone %}
<tr>
<th style="..." scope="..." colspan="...">{{appt.scheduled_start}}</th>
<td style="...">{{appt.task.name}}</td>
<td style="...">{{appt.task.property.name}}</td>

```


---

```django

<tr>
<th style="..." scope="..." colspan="...">{{appt.scheduled_start}}</th>
<td style="...">{{appt.task.name}}</td>
<td style="...">{{appt.task.property.name}}</td>
</tr>

```

</details>

---

## attention

<details class="expandable-section">
<summary><strong>Found in files</strong></summary>

- [AARHUSFIRE] - [emails] - [Defect Quote Summary Reminder Email](https://AARHUSFIRE.onuptick.com/configuration/emails)
- [AARHUSFIRE] - [emails] - [Issuance](https://AARHUSFIRE.onuptick.com/configuration/emails)
- [AARHUSFIRE] - [emails] - [Service Quote Issued Email](https://AARHUSFIRE.onuptick.com/configuration/emails)

</details>

<details class="expandable-section">
<summary><strong>Usage Examples</strong></summary>

```django

{% load getattr %}
{% block content %}
<p>Dear {{ attention|default:"Manager" }},</p>
<p>You have been selected as the main recipient or a CC in this repeating reminder.</p>
<p>We are waiting for approval for the following defect quotes:</p>

```


---

```django

<p>
Dear {{ attention|default:'valued customer' }},
</p>
<p>

```

</details>

---

## base_url

<details class="expandable-section">
<summary><strong>Found in files</strong></summary>

- [AARHUSFIRE] - [emails] - [Monthly Uncovered Assets](https://AARHUSFIRE.onuptick.com/configuration/emails)

</details>

<details class="expandable-section">
<summary><strong>Usage Examples</strong></summary>

```django

<ul>
{% for property in properties %}
<li><a href="{{base_url}}/properties/{{property.property_id}}/view/assets/?is_covered_by_routine=False&is_active=True">{{ property.property__name }}</a></li>
{% endfor %}
</ul>

```

</details>

---

## before_photos

<details class="expandable-section">
<summary><strong>Found in files</strong></summary>

- [AARHUSFIRE] - [templates] - [Service Report (Prompts)](https://AARHUSFIRE.onuptick.com/configuration/templates)
- [ABACUSFAS] - [emails] - [test](https://ABACUSFAS.onuptick.com/configuration/emails)

</details>

<details class="expandable-section">
<summary><strong>Usage Examples</strong></summary>

```django

{% endif %}
<div class="...">
{% for photo in before_photos %}
{% include "webtemplates/2022-photo-tile" with photo=photo class="..." %}
{% endfor %}

```

</details>

---

## client

<details class="expandable-section">
<summary><strong>Found in files</strong></summary>

- [AARHUSFIRE] - [emails] - [Service Quote Reminder Email](https://AARHUSFIRE.onuptick.com/configuration/emails)

</details>

### Properties

| Property | Example Usage |
|----------|---------------|
| `name` | {{ client.name\|default:'valued customer' }} |

<details class="expandable-section">
<summary><strong>Usage Examples</strong></summary>

```django

<p>Dear {{ client.name|default:'valued customer' }},</p>
<p>This is a friendly reminder that we’re awaiting your quote approval for {{ property }}.</p>
{% if servicequote.description %}

```

</details>

---

## consolidated_tasks

<details class="expandable-section">
<summary><strong>Found in files</strong></summary>

- [AARHUSFIRE] - [templates] - [Consolidated Invoice](https://AARHUSFIRE.onuptick.com/configuration/templates)
- [AARHUSFIRE] - [templates] - [Invoice](https://AARHUSFIRE.onuptick.com/configuration/templates)
- [AARHUSFIRE] - [templates] - [Service Quote (Totals only)](https://AARHUSFIRE.onuptick.com/configuration/templates)
- [AARHUSFIRE] - [templates] - [Service Report (Prompts)](https://AARHUSFIRE.onuptick.com/configuration/templates)
- [ABACUSFAS] - [emails] - [test](https://ABACUSFAS.onuptick.com/configuration/emails)

</details>

### Properties

| Property | Example Usage |
|----------|---------------|
| `COMPANY_LICENSES` | {{ consolidated_tasks.COMPANY_LICENSES\|markdowner }} |
| `INVOICE_PAYMENT_INSTRUCTIONS` | {{ consolidated_tasks.INVOICE_PAYMENT_INSTRUCTIONS\|markdowner\|default:"Please pay invoice by the due date" }} |
| `SERVICEQUOTE_TEMPLATE_TERMS_AND_CONDITIONS` | {{ consolidated_tasks.SERVICEQUOTE_TEMPLATE_TERMS_AND_CONDITIONS\|markdowner }} |
| `SITE_ABN` | {{ consolidated_tasks.SITE_ABN }} |

<details class="expandable-section">
<summary><strong>Usage Examples</strong></summary>

```django

<small>
<strong class="...">Company Accreditations:</strong>
<div class="...">{{ config.COMPANY_LICENSES|markdowner }}</div>
</small>
</section>

```


---

```django

<p>{{ config.SITE_ABN }}</p>
<h6>Payment instructions</h6>
{{ config.INVOICE_PAYMENT_INSTRUCTIONS|markdowner|default:"Please pay invoice by the due date" }}
</section>
{% endblock %}

```

</details>

---

## creditnotes

<details class="expandable-section">
<summary><strong>Found in files</strong></summary>

- [AARHUSFIRE] - [templates] - [Consolidated Invoice](https://AARHUSFIRE.onuptick.com/configuration/templates)

</details>

### Properties

| Property | Example Usage |
|----------|---------------|
| `number` | {{ note.number }} |
| `total` | {{ note.total\|currency }} |

<details class="expandable-section">
<summary><strong>Usage Examples</strong></summary>

```django

</tr>
{% if creditnotes %}
{% for note in creditnotes %}
<tr>
<th class="...">Credit {{ note.number }} - {{ note }}</th>

```

</details>

---

## defectquotes

<details class="expandable-section">
<summary><strong>Found in files</strong></summary>

- [AARHUSFIRE] - [emails] - [Issuance](https://AARHUSFIRE.onuptick.com/configuration/emails)

</details>

### Properties

| Property | Example Usage |
|----------|---------------|
| `get_uuid_approval_url` | {{ quote.get_uuid_approval_url }} |
| `ref` | {{ quote.ref }} |

<details class="expandable-section">
<summary><strong>Usage Examples</strong></summary>

```django

<p>Your defect quotes:</p>
<ul>
{% for quote in defectquotes %}
<li>Reference: {{ quote.ref }}<a href="{{ base_url }}{{ quote.get_uuid_approval_url }}"> (approve online)</a></li>
{% endfor %}

```

</details>

---

## digital_logbooks

<details class="expandable-section">
<summary><strong>Found in files</strong></summary>

- [AARHUSFIRE] - [templates] - [Service Report (Prompts)](https://AARHUSFIRE.onuptick.com/configuration/templates)
- [AARHUSFIRE] - [emails] - [Issuance](https://AARHUSFIRE.onuptick.com/configuration/emails)
- [ABACUSFAS] - [emails] - [test](https://ABACUSFAS.onuptick.com/configuration/emails)

</details>

### Properties

| Property | Example Usage |
|----------|---------------|
| `name` | {{ logbook.name }} |
| `url` | {{ entry.url }} |

<details class="expandable-section">
<summary><strong>Usage Examples</strong></summary>

```django

</div>
{% endfor %}
{% for entry in digital_logbooks %}
<div class="...">
<div class="...">

```


---

```django

<p>Your attached digital logbook entries:</p>
<ul>
{% for logbook in digital_logbooks %}
<li>{{ logbook.name }}</li>
{% endfor %}

```

</details>

---

## doandchargelineitems

<details class="expandable-section">
<summary><strong>Found in files</strong></summary>

- [AARHUSFIRE] - [templates] - [Service Quote (Routines)](https://AARHUSFIRE.onuptick.com/configuration/templates)
- [AARHUSFIRE] - [templates] - [Service Quote (Totals only)](https://AARHUSFIRE.onuptick.com/configuration/templates)

</details>

<details class="expandable-section">
<summary><strong>Usage Examples</strong></summary>

```django

</thead>
<tbody>
{% for line in doandchargelineitems %}
<tr class="...">
<td>

```

</details>

---

## email

<details class="expandable-section">
<summary><strong>Found in files</strong></summary>

- [AARHUSFIRE] - [emails] - [Defect Quote Summary Reminder Email](https://AARHUSFIRE.onuptick.com/configuration/emails)

</details>

<details class="expandable-section">
<summary><strong>Usage Examples</strong></summary>

```django

{% for email in quote_email_lookup|getvalue:quote %}
{% if email != recipient %}
<li>{{email}}</li>
{% endif %}
{% endfor %}

```

</details>

---

## entry

<details class="expandable-section">
<summary><strong>Found in files</strong></summary>

- [AARHUSFIRE] - [templates] - [Service Report (Prompts)](https://AARHUSFIRE.onuptick.com/configuration/templates)
- [ABACUSFAS] - [emails] - [test](https://ABACUSFAS.onuptick.com/configuration/emails)

</details>

### Properties

| Property | Example Usage |
|----------|---------------|
| `files` | {% for file in entry.files %} |
| `logbook` | {{ entry.logbook.name\|default:'-' }} |
| `logbook.name` | {{ entry.logbook.name\|default:'-' }} |
| `preview_url` | {{ file.preview_url }} |
| `url` | {{ entry.url }} |

<details class="expandable-section">
<summary><strong>Usage Examples</strong></summary>

```django

<div class="...">
<a href="{{ entry.url }}">
<strong>{{ entry.logbook.name|default:'-' }}</strong>
{% include "reports/library/arrow-up-right-from-square-icon.svg" with width="..." height="..." %}
</a>

```


---

```django

<div class="...">
<strong>{{ entry.logbook.name|default:'-' }}</strong>
{% for file in entry.files %}
<a class="..." href="{{ file.preview_url }}">
{% include "reports/library/arrow-up-right-from-square-icon.svg" with width="..." height="..." %}

```

</details>

---

## fixedlineitems

<details class="expandable-section">
<summary><strong>Found in files</strong></summary>

- [AARHUSFIRE] - [templates] - [Service Quote (Totals only)](https://AARHUSFIRE.onuptick.com/configuration/templates)

</details>

<details class="expandable-section">
<summary><strong>Usage Examples</strong></summary>

```django

</thead>
<tbody>
{% for line in fixedlineitems %}
<tr class="...">
<td>

```

</details>

---

## formresponses

<details class="expandable-section">
<summary><strong>Found in files</strong></summary>

- [AARHUSFIRE] - [emails] - [Issuance](https://AARHUSFIRE.onuptick.com/configuration/emails)

</details>

<details class="expandable-section">
<summary><strong>Usage Examples</strong></summary>

```django

{% endif %}
<ul>
{% for formresponse in formresponses %}
<li>{{ formresponse }}</li>
{% endfor %}

```

</details>

---

## invoices

<details class="expandable-section">
<summary><strong>Found in files</strong></summary>

- [AARHUSFIRE] - [templates] - [Consolidated Invoice](https://AARHUSFIRE.onuptick.com/configuration/templates)
- [AARHUSFIRE] - [templates] - [Invoice](https://AARHUSFIRE.onuptick.com/configuration/templates)
- [AARHUSFIRE] - [emails] - [Issuance](https://AARHUSFIRE.onuptick.com/configuration/emails)
- [AARHUSFIRE] - [emails] - [Overdue Invoice Reminder Email](https://AARHUSFIRE.onuptick.com/configuration/emails)

</details>

### Properties

| Property | Example Usage |
|----------|---------------|
| `billingcard` | {{ invoices.billingcard.postal_address\|linebreaksbr }} |
| `billingcard.postal_address` | {{ invoices.billingcard.postal_address\|linebreaksbr }} |
| `date` | {{ invoices.date\|date:"jS F Y"\|default:"-" }} |
| `description` | {{ invoices.description\|markdowner }} |
| `due_date` | {{ invoices.due_date\|date:"jS F Y" }} |
| `gst` | {{ invoices.gst\|currency }} |
| `number` | {{ inv.number }} |
| `ref` | {{ invoices.ref\|default:"-" }} |
| `subtotal` | {{ invoices.subtotal\|currency }} |
| `total` | {{ invoices.total\|currency }} |
| `total_after_credits` | {{ invoices.total_after_credits\|currency }} |

<details class="expandable-section">
<summary><strong>Usage Examples</strong></summary>

```django

<p>Your invoice:</p>
<ul>
<li>{{ invoice.number|default:"[[ invoice_number ]]" }} {% if invoice.ref %}({{ invoice.ref }}){% endif %}</li>
</ul>
{% endif %}

```


---

```django

Number: {{ inv.number }}<br>
Reference: {{ inv.ref }}<br>
Due: {{ inv.due_date|date:"jS F Y" }}<br>
{% endfor %}
For any questions please contact the office.</p>

```

</details>

---

## items

<details class="expandable-section">
<summary><strong>Found in files</strong></summary>

- [AARHUSFIRE] - [emails] - [Signoff Disclaimed](https://AARHUSFIRE.onuptick.com/configuration/emails)

</details>

### Properties

| Property | Example Usage |
|----------|---------------|
| `label` | {{ item.label }} |

<details class="expandable-section">
<summary><strong>Usage Examples</strong></summary>

```django

<p>We have received notification from {{ contractor.name }} that they are no longer engaged to maintain the following items:</p>
<ul>
{% for item in items %}
<li>{{ item.label }}</li>
{% endfor %}

```

</details>

---

## joyfillformresponses

<details class="expandable-section">
<summary><strong>Found in files</strong></summary>

- [AARHUSFIRE] - [emails] - [Issuance](https://AARHUSFIRE.onuptick.com/configuration/emails)

</details>

<details class="expandable-section">
<summary><strong>Usage Examples</strong></summary>

```django

{% endif %}
<ul>
{% for formresponse in joyfillformresponses %}
<li>{{ formresponse }}</li>
{% endfor %}

```

</details>

---

## labour_sessions

<details class="expandable-section">
<summary><strong>Found in files</strong></summary>

- [AARHUSFIRE] - [templates] - [Service Report (Prompts)](https://AARHUSFIRE.onuptick.com/configuration/templates)
- [ABACUSFAS] - [emails] - [test](https://ABACUSFAS.onuptick.com/configuration/emails)

</details>

### Properties

| Property | Example Usage |
|----------|---------------|
| `finished` | {{ tasksession.finished\|timezone:tasksession.timezone\|date:'H:i'\|default:"(still in progress)" }} |
| `get_duration` | {{ tasksession.get_duration\|duration }} |
| `get_type_display` | {{ tasksession.get_type_display }} |
| `started` | {{ tasksession.started\|timezone:tasksession.timezone\|date:'d/m/Y H:i' }} |
| `technician` | {{ tasksession.technician }} |

<details class="expandable-section">
<summary><strong>Usage Examples</strong></summary>

```django

</thead>
<tbody>
{% for tasksession in labour_sessions %}
<tr>
<td>{{ tasksession.get_type_display }}</td>

```

</details>

---

## lineitem_group

<details class="expandable-section">
<summary><strong>Found in files</strong></summary>

- [AARHUSFIRE] - [templates] - [Consolidated Invoice](https://AARHUSFIRE.onuptick.com/configuration/templates)
- [AARHUSFIRE] - [templates] - [Invoice](https://AARHUSFIRE.onuptick.com/configuration/templates)
- [AARHUSFIRE] - [templates] - [Itemised w Prices	](https://AARHUSFIRE.onuptick.com/configuration/templates)
- [AARHUSFIRE] - [templates] - [Itemised w Qty	](https://AARHUSFIRE.onuptick.com/configuration/templates)
- [AARHUSFIRE] - [templates] - [Purchase Order](https://AARHUSFIRE.onuptick.com/configuration/templates)
- [AARHUSFIRE] - [templates] - [Service Quote (Routines)](https://AARHUSFIRE.onuptick.com/configuration/templates)
- [AARHUSFIRE] - [templates] - [Service Quote (Totals only)](https://AARHUSFIRE.onuptick.com/configuration/templates)

</details>

### Properties

| Property | Example Usage |
|----------|---------------|
| `annual_subtotal` | {{ lineitem_group.annual_subtotal\|currency }} |
| `asset` | {{ lineitem_group.asset.get_label\|default:"General Repairs" }} |
| `asset.get_label` | {{ lineitem_group.asset.get_label\|default:"General Repairs" }} |
| `cost_summary` | {{ lineitem_group.cost_summary.gst\|currency }} |
| `cost_summary.gst` | {{ lineitem_group.cost_summary.gst\|currency }} |
| `cost_summary.subtotal` | {{ lineitem_group.cost_summary.subtotal\|currency }} |
| `cost_summary.total` | {{ lineitem_group.cost_summary.total\|currency }} |
| `description` | {{ line.description\|markdowner }} |
| `gst` | {{ lineitem.gst\|currency }} |
| `lineitems` | {% for lineitem in lineitem_group.lineitems %} |
| `name` | {{ rslt.name }} |
| `property` | {{ lineitem_group.property.client_ref}} |
| `property.client_ref` | {{ lineitem_group.property.client_ref}} |
| `quantity` | {{ lineitem_group.quantity\|floatformat:2 }} |
| `remark` | {{ lineitem_group.remark.get_resolution\|markdowner }} |
| `remark.get_description` | {{ lineitem_group.remark.get_description\|markdowner }} |
| `remark.get_public_url` | {{ lineitem_group.remark.get_public_url\|absolute }} |
| `remark.get_resolution` | {{ lineitem_group.remark.get_resolution\|markdowner }} |
| `remark.location` | {{ lineitem_group.remark.location\|markdowner }} |
| `routineserviceleveltypes` | {% for rslt in lineitem_group.routineserviceleveltypes.all %} |
| `routineserviceleveltypes.all` | {% for rslt in lineitem_group.routineserviceleveltypes.all %} |
| `site_price` | {{ lineitem_group.site_price\|currency }} |
| `subtotal` | {{ lineitem_group.subtotal\|currency }} |
| `task` | {{ lineitem_group.task.scope_of_works\|markdowner }} |
| `task.description` | {{ lineitem_group.task.description\|markdowner }} |
| `task.invoice_note` | {{ lineitem_group.task.invoice_note\|markdowner }} |
| `task.scope_of_works` | {{ lineitem_group.task.scope_of_works\|markdowner }} |
| `unit_price` | {{ line.unit_price\|currency }} |

<details class="expandable-section">
<summary><strong>Usage Examples</strong></summary>

```django

<td colspan="...">
<div>
<strong>{{ lineitem.asset.get_label|default:"General Repairs" }}</strong>
<div>{{ lineitem.asset.location }}</div>
</div>

```


---

```django

<strong>{{ lineitem.remark.get_severity_display }}</strong>
<div>
<a href="{{ lineitem.remark.get_public_url|absolute }}">
ID: {{ lineitem.remark.id }}
{% include "reports/library/arrow-up-right-from-square-icon.svg" with width="..." height="..." %}

```

</details>

---

## maintenance_technicians

<details class="expandable-section">
<summary><strong>Found in files</strong></summary>

- [AARHUSFIRE] - [templates] - [Service Report (Prompts)](https://AARHUSFIRE.onuptick.com/configuration/templates)
- [ABACUSFAS] - [emails] - [test](https://ABACUSFAS.onuptick.com/configuration/emails)

</details>

### Properties

| Property | Example Usage |
|----------|---------------|
| `asset` | {{ row.asset }} |
| `count` | {{ row.count }} |
| `inspected_date` | {{ technician.inspected_date }} |
| `name` | {{ technician.name }} |
| `service` | {{ row.service }} |

<details class="expandable-section">
<summary><strong>Usage Examples</strong></summary>

```django

</thead>
<tbody>
{% for row in maintenance_summary %}
<tr>
<td>{{ row.service }}</td>

```


---

```django

</thead>
<tbody>
{% for technician in maintenance_technicians %}
<tr>
<td>{{ technician.name }}</td>

```

</details>

---

## note

<details class="expandable-section">
<summary><strong>Found in files</strong></summary>

- [AARHUSFIRE] - [templates] - [Consolidated Invoice](https://AARHUSFIRE.onuptick.com/configuration/templates)

</details>

### Properties

| Property | Example Usage |
|----------|---------------|
| `number` | {{ note.number }} |
| `total` | {{ note.total\|currency }} |

<details class="expandable-section">
<summary><strong>Usage Examples</strong></summary>

```django

<tr>
<th class="...">Credit {{ note.number }} - {{ note }}</th>
<td class="...">{{ note.total|currency }}</td>
</tr>
{% endfor %}

```

</details>

---

## paper_logbooks

<details class="expandable-section">
<summary><strong>Found in files</strong></summary>

- [AARHUSFIRE] - [templates] - [Service Report (Prompts)](https://AARHUSFIRE.onuptick.com/configuration/templates)
- [AARHUSFIRE] - [emails] - [Corrigo Webhook Event Rejection](https://AARHUSFIRE.onuptick.com/configuration/emails)
- [ABACUSFAS] - [emails] - [test](https://ABACUSFAS.onuptick.com/configuration/emails)

</details>

<details class="expandable-section">
<summary><strong>Usage Examples</strong></summary>

```django

<div class="...">Logbooks</div>
<div class="...">
{% for entry in paper_logbooks %}
<div class="...">
<div class="...">

```


---

```django

<p>Reason: {{ message }}</p>
<p>Payload:<p>
<pre><code>{{payload}}</code></pre>
<p>Regards,<br >Uptick Team</p>

```

</details>

---

## photos

<details class="expandable-section">
<summary><strong>Found in files</strong></summary>

- [AARHUSFIRE] - [templates] - [Itemised w Prices	](https://AARHUSFIRE.onuptick.com/configuration/templates)
- [AARHUSFIRE] - [templates] - [Itemised w Qty	](https://AARHUSFIRE.onuptick.com/configuration/templates)

</details>

<details class="expandable-section">
<summary><strong>Usage Examples</strong></summary>

```django

{% if photos %}
<div class="...">
{% for photo in photos %}
{% include "webtemplates/2022-photo-tile" with photo=photo class="..." %}
{% endfor %}

```

</details>

---

## productlineitems

<details class="expandable-section">
<summary><strong>Found in files</strong></summary>

- [AARHUSFIRE] - [templates] - [Service Quote (Routines)](https://AARHUSFIRE.onuptick.com/configuration/templates)
- [AARHUSFIRE] - [templates] - [Service Quote (Totals only)](https://AARHUSFIRE.onuptick.com/configuration/templates)
- [AARHUSFIRE] - [emails] - [Monthly Uncovered Assets](https://AARHUSFIRE.onuptick.com/configuration/emails)
- [AARHUSFIRE] - [emails] - [Signoff Generation Notification Email](https://AARHUSFIRE.onuptick.com/configuration/emails)

</details>

### Properties

| Property | Example Usage |
|----------|---------------|
| `description` | {{ line.description\|default:'-' }} |
| `property__name` | {{ productlineitems.productlineitems__name }} |
| `property_id` | {{productlineitems.productlineitems_id}} |
| `quantity` | {{ line.quantity\|floatformat:2 }} |
| `subtotal` | {{ line.subtotal\|currency }} |
| `unit_price` | {{ line.unit_price\|currency }} |

<details class="expandable-section">
<summary><strong>Usage Examples</strong></summary>

```django

<ul>
{% for property in properties %}
<li><a href="{{base_url}}/properties/{{property.property_id}}/view/assets/?is_covered_by_routine=False&is_active=True">{{ property.property__name }}</a></li>
{% endfor %}
</ul>

```


---

```django

<p>There are currently {{ no_of_assets }} assets not covered by any Routines. These assets relate to the following properties:</p>
<ul>
{% for property in properties %}
<li><a href="{{base_url}}/properties/{{property.property_id}}/view/assets/?is_covered_by_routine=False&is_active=True">{{ property.property__name }}</a></li>
{% endfor %}

```

</details>

---

## purchaseorder

<details class="expandable-section">
<summary><strong>Found in files</strong></summary>

- [AARHUSFIRE] - [templates] - [Purchase Order](https://AARHUSFIRE.onuptick.com/configuration/templates)

</details>

### Properties

| Property | Example Usage |
|----------|---------------|
| `created` | {{ purchaseorder.created\|date:"jS F Y" }} |
| `currency` | {{ purchaseorder.currency }} |
| `delivery_instructions` | {{ purchaseorder.delivery_instructions\|markdowner }} |
| `description` | {{ purchaseorder.description\|markdowner }} |
| `gst` | {{ purchaseorder.gst\|currency }} |
| `subtotal` | {{ purchaseorder.subtotal\|currency }} |
| `total` | {{ purchaseorder.total\|currency }} |

<details class="expandable-section">
<summary><strong>Usage Examples</strong></summary>

```django

<div class="...">
<div class="...">
{{ purchaseorder.description|markdowner }}
{% if purchaseorder.delivery_instructions %}
<dl>

```


---

```django

<dl>
<dt>Delivery instructions</dt>
<dd>{{ purchaseorder.delivery_instructions|markdowner }}</dd>
</dl>
{% endif %}

```

</details>

---

## quotes

<details class="expandable-section">
<summary><strong>Found in files</strong></summary>

- [AARHUSFIRE] - [templates] - [Itemised w Prices	](https://AARHUSFIRE.onuptick.com/configuration/templates)
- [AARHUSFIRE] - [templates] - [Itemised w Qty	](https://AARHUSFIRE.onuptick.com/configuration/templates)
- [AARHUSFIRE] - [emails] - [Defect Quote Summary Reminder Email](https://AARHUSFIRE.onuptick.com/configuration/emails)

</details>

### Properties

| Property | Example Usage |
|----------|---------------|
| `get_uuid_approval_url` | {{ quote.get_uuid_approval_url }} |
| `gst` | {{quotes.gst\|currency}} |
| `ref` | {{ quote.ref }} |
| `subtotal` | {{quotes.subtotal\|currency}} |
| `total` | {{quotes.total\|currency}} |

<details class="expandable-section">
<summary><strong>Usage Examples</strong></summary>

```django

<p>You have been selected as the main recipient or a CC in this repeating reminder.</p>
<p>We are waiting for approval for the following defect quotes:</p>
{% for quote in quotes %}
<p>
<div>Reference: {{ quote.ref }}</div>

```


---

```django

<tr>
<td width="..." class="..."><strong>Subtotal </strong></td>
<td width="...">{{quote.subtotal|currency}}</td>
</tr>
<tr>

```

</details>

---

## rectification

<details class="expandable-section">
<summary><strong>Found in files</strong></summary>

- [AARHUSFIRE] - [templates] - [Service Report (Prompts)](https://AARHUSFIRE.onuptick.com/configuration/templates)
- [AARHUSFIRE] - [emails] - [Appointment Scheduled Email](https://AARHUSFIRE.onuptick.com/configuration/emails)
- [AARHUSFIRE] - [emails] - [Issuance](https://AARHUSFIRE.onuptick.com/configuration/emails)
- [AARHUSFIRE] - [emails] - [Overdue Invoice Reminder Email](https://AARHUSFIRE.onuptick.com/configuration/emails)
- [AARHUSFIRE] - [emails] - [Rectification Rejected](https://AARHUSFIRE.onuptick.com/configuration/emails)
- [ABACUSFAS] - [emails] - [test](https://ABACUSFAS.onuptick.com/configuration/emails)

</details>

### Properties

| Property | Example Usage |
|----------|---------------|
| `asset` | {{ rectification.asset.get_label\|default:"General Repairs" }} |
| `asset.get_label` | {{ rectification.asset.get_label\|default:"General Repairs" }} |
| `compliant` | {{ rectification.compliant\|yesno:"compliant,non-compliant,not applicable"}} |
| `email` | {{rectification.email}} |
| `get_title` | {{ rectification.get_title }} |
| `name` | {{rectification.name}} |
| `notes` | {{ rectification.notes\|default:rectification.product.description\|default:rectification.product.name }} |
| `quantity` | {{ rectification.quantity\|floatformat:2 }} |
| `ref` | {{ rectification.ref }} |
| `rejection_reason` | {{ rectification.rejection_reason\|markdowner }} |
| `remark` | {{ rectification.remark.location\|markdowner }} |
| `remark.get_description` | {{ rectification.remark.get_description\|markdowner }} |
| `remark.get_public_url` | {{ rectification.remark.get_public_url\|absolute }} |
| `remark.get_resolution` | {{ rectification.remark.get_resolution\|markdowner }} |
| `remark.location` | {{ rectification.remark.location\|markdowner }} |

<details class="expandable-section">
<summary><strong>Usage Examples</strong></summary>

```django

<tr class="...">
<td colspan="...">
<strong>{{ repair.asset.get_label|default:"General Repairs" }}</strong>
<div>{{ repair.asset.location }}</div>
</td>

```


---

```django

<strong>{{ repair.remark.get_severity_display }}</strong>
<div>
<a href="{{ repair.remark.get_public_url|absolute }}">
ID: {{ repair.remark.id }}
{% include "reports/library/arrow-up-right-from-square-icon.svg" with width="..." height="..." %}

```

</details>

---

## servicelineitems

<details class="expandable-section">
<summary><strong>Found in files</strong></summary>

- [AARHUSFIRE] - [templates] - [Service Quote (Routines)](https://AARHUSFIRE.onuptick.com/configuration/templates)
- [AARHUSFIRE] - [templates] - [Service Quote (Totals only)](https://AARHUSFIRE.onuptick.com/configuration/templates)

</details>

### Properties

| Property | Example Usage |
|----------|---------------|
| `annual_gst` | {{ servicelineitems.annual_gst\|currency }} |
| `annual_subtotal` | {{ servicelineitems.annual_subtotal\|currency }} |
| `annual_tax` | {{ servicelineitems.annual_tax\|currency }} |
| `annual_total` | {{ servicelineitems.annual_total\|currency }} |
| `created` | {{ servicelineitems.created\|date:"jS F Y" }} |
| `expiry_date` | {{ servicelineitems.expiry_date }} |
| `product_gst` | {{ servicelineitems.product_gst\|currency }} |
| `product_subtotal` | {{ servicelineitems.product_subtotal\|currency }} |
| `product_total` | {{ servicelineitems.product_total\|currency }} |
| `ref` | {{ servicelineitems.ref }} |
| `scope_of_works` | {{ servicelineitems.scope_of_works\|markdowner }} |
| `terms_and_conditions` | {{ servicelineitems.terms_and_conditions\|markdowner }} |

<details class="expandable-section">
<summary><strong>Usage Examples</strong></summary>

```django

<section class="...">
<h2 class="...">Service Quotation <strong>{{ servicequote.ref }}</strong></h2>
<div>{{ servicequote.created|date:"jS F Y" }}</div>
{% if servicequote.expiry_date %}<div>This quote is valid until <em>{{ servicequote.expiry_date }}</em></div>{% endif %}
<div><strong>Attention: {{ client.primary_contact.name }}</strong></div>

```


---

```django

{% if servicequote.scope_of_works %}
<div class="...">
{{ servicequote.scope_of_works|markdowner }}
</div>
{% endif %}

```

</details>

---

## show_rate_column

<details class="expandable-section">
<summary><strong>Found in files</strong></summary>

- [AARHUSFIRE] - [templates] - [Purchase Order](https://AARHUSFIRE.onuptick.com/configuration/templates)

</details>

<details class="expandable-section">
<summary><strong>Usage Examples</strong></summary>

```django

<th class="..." width="...">Unit Price</th>
<th class="..." width="...">Subtotal</th>
<th class="..." width="..."100,0" }}">
{% if show_rate_column %}{% get_tax_summary_name %} Rate{% endif %}
</th>

```

</details>

---

## signoffproperties

<details class="expandable-section">
<summary><strong>Found in files</strong></summary>

- [AARHUSFIRE] - [templates] - [Service Report (Prompts)](https://AARHUSFIRE.onuptick.com/configuration/templates)
- [AARHUSFIRE] - [emails] - [Signoff Disclaimed](https://AARHUSFIRE.onuptick.com/configuration/emails)
- [AARHUSFIRE] - [emails] - [Signoff Reminder](https://AARHUSFIRE.onuptick.com/configuration/emails)
- [AARHUSFIRE] - [emails] - [Signoff Request](https://AARHUSFIRE.onuptick.com/configuration/emails)
- [AARHUSFIRE] - [emails] - [Signoff Response](https://AARHUSFIRE.onuptick.com/configuration/emails)
- [ABACUSFAS] - [emails] - [test](https://ABACUSFAS.onuptick.com/configuration/emails)

</details>

### Properties

| Property | Example Usage |
|----------|---------------|
| `account` | {{ signoffproperties.account }} |
| `contractor` | {{ signoffproperties.contractor }} |
| `created` | {{ signoffproperties.created\|date }} |
| `disclaimed_reason` | {{signoffproperties.disclaimed_reason}} |
| `due` | {{ signoffproperty.due\|date }} |
| `filename` | {{ signature.filename }} |
| `is_disclaimed` | {{ signoffproperties.is_disclaimed\|yesno:"red,black" }} |
| `label` | {{ signoffitem.label }} |
| `new_is_compliant` | {{ signoffitem.new_is_compliant\|yesno:"compliant,non-compliant" }} |
| `new_serviced_date` | {{ signoffitem.new_serviced_date }} |
| `new_signoff_note` | {{ signoffitem.new_signoff_note }} |
| `note` | {{ signoffproperties.note }} |
| `period_finish` | {{ signoffproperties.period_finish }} |
| `period_start` | {{ signoffproperties.period_start}} |
| `pk` | {{ signoffproperties.pk }} |
| `property` | {{ signoffproperties.property }} |
| `signoffitem_set` | {% for signoffitem in signoffproperties.signoffitem_set.all %} |
| `signoffitem_set.all` | {% for signoffitem in signoffproperties.signoffitem_set.all %} |
| `signoffproperty_set` | {% for signoffpropertiesproperty in signoffproperties.signoffpropertiesproperty_set.all %} |
| `signoffproperty_set.all` | {% for signoffpropertiesproperty in signoffproperties.signoffpropertiesproperty_set.all %} |

<details class="expandable-section">
<summary><strong>Usage Examples</strong></summary>

```django

<div class="...">Signatures</div>
<div class="...">
{% for signature in signatures %}
<div class="...">
<div class="...">{% cdn_image signature.path height=100 crop="fill" type="authenticated" %}</div>

```


---

```django

{% extends 'email.html' %}
{% block content %}
<h4>Request{{ signoffproperties|pluralize }} for {{ contractor.name }} ({{ contractor.account }}).</h4>
<p>In order to issue compliant reports, we require confirmation that you, as a service contractor, have serviced the relevant Essential Safety Measures to Australian Standards over the previous 12 months.</p>
<table border="..." cellpadding="..." cellspacing="..." bgcolor="..." width="...">

```

</details>

---

## summary_remarks

<details class="expandable-section">
<summary><strong>Found in files</strong></summary>

- [AARHUSFIRE] - [templates] - [Itemised w Prices	](https://AARHUSFIRE.onuptick.com/configuration/templates)
- [AARHUSFIRE] - [templates] - [Itemised w Qty	](https://AARHUSFIRE.onuptick.com/configuration/templates)
- [AARHUSFIRE] - [templates] - [Service Report (Prompts)](https://AARHUSFIRE.onuptick.com/configuration/templates)
- [ABACUSFAS] - [emails] - [test](https://ABACUSFAS.onuptick.com/configuration/emails)

</details>

### Properties

| Property | Example Usage |
|----------|---------------|
| `0` | {{ summary_remarks.0\|default:"0" }} |
| `1` | {{ summary_remarks.1\|default:"0" }} |
| `10` | {{ summary_remarks.10\|default:"0" }} |
| `2` | {{ summary_remarks.2\|default:"0" }} |
| `5` | {{ summary_remarks.5\|default:"0" }} |

<details class="expandable-section">
<summary><strong>Usage Examples</strong></summary>

```django

<tbody>
<tr>
<td width="..." class="..."><strong>{{ summary_remarks.10|default:"0" }}</strong></td>
<td width="..." class="..."><strong>Critical Defects</strong></td>
<td width="..." class="...">A defect that renders a system inoperative.</td>

```


---

```django

</tr>
<tr>
<td class="..."><strong>{{ summary_remarks.5|default:"0" }}</strong></td>
<td class="..."><strong>Non-critical Defects</strong></td>
<td class="...">A system impairment not likely to critically affect the operation of the system.</td>

```

</details>

---

## task_origin_defectquote

<details class="expandable-section">
<summary><strong>Found in files</strong></summary>

- [AARHUSFIRE] - [templates] - [Service Report (Prompts)](https://AARHUSFIRE.onuptick.com/configuration/templates)
- [AARHUSFIRE] - [emails] - [Bulk Contractor Contact Task Assignment Email](https://AARHUSFIRE.onuptick.com/configuration/emails)
- [AARHUSFIRE] - [emails] - [Task Assigned Email](https://AARHUSFIRE.onuptick.com/configuration/emails)
- [ABACUSFAS] - [emails] - [test](https://ABACUSFAS.onuptick.com/configuration/emails)

</details>

### Properties

| Property | Example Usage |
|----------|---------------|
| `address` | {{ task.address }} |
| `description` | {{ task.description }} |
| `finished` | {{ task_origin_defectquote.finished\|timezone:task_origin_defectquote.timezone\|date:'H:i'\|default:"(still in progress)" }} |
| `get_duration` | {{ task_origin_defectquote.get_duration\|duration }} |
| `get_type_display` | {{ task_origin_defectquote.get_type_display }} |
| `get_uuid_approval_url` | {{ task_origin_defectquote.get_uuid_approval_url\|absolute }} |
| `ref` | {{ task_origin_defectquote.ref }} |
| `started` | {{ task_origin_defectquote.started\|timezone:task_origin_defectquote.timezone\|date:'d/m/Y H:i' }} |
| `technician` | {{ task_origin_defectquote.technician }} |

<details class="expandable-section">
<summary><strong>Usage Examples</strong></summary>

```django

{% if task_origin_defectquote.ref %}
<div class="...">
<a href="{{ task_origin_defectquote.get_uuid_approval_url|absolute }}">
{{ task_origin_defectquote.ref }}
{% include "reports/library/arrow-up-right-from-square-icon.svg" with width="..." height="..." %}

```


---

```django

<td>{{ tasksession.get_type_display }}</td>
<td>{{ tasksession.technician }}</td>
<td>{{ tasksession.started|timezone:tasksession.timezone|date:'d/m/Y H:i' }} -
{{ tasksession.finished|timezone:tasksession.timezone|date:'H:i'|default:"(still in progress)" }}</td>
<td>{{ tasksession.get_duration|duration }}</td>

```

</details>

---

## technician

<details class="expandable-section">
<summary><strong>Found in files</strong></summary>

- [AARHUSFIRE] - [templates] - [Service Report (Prompts)](https://AARHUSFIRE.onuptick.com/configuration/templates)
- [ABACUSFAS] - [emails] - [test](https://ABACUSFAS.onuptick.com/configuration/emails)

</details>

### Properties

| Property | Example Usage |
|----------|---------------|
| `accreditations` | {% for accreditation in technician.accreditations %} |
| `inspected_date` | {{ technician.inspected_date }} |
| `name` | {{accreditation.name}} |
| `number` | {{ accreditation.number }} |

<details class="expandable-section">
<summary><strong>Usage Examples</strong></summary>

```django

<td>{{ technician.inspected_date }}</td>
<td>
{% for accreditation in technician.accreditations %}
<div>{{accreditation.name}}: {{ accreditation.number }}</div>
{% endfor %}

```

</details>

---


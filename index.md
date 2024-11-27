---
title: Django Template Variables Documentation
layout: default
---


<style>
body {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Arial, sans-serif;
    line-height: 1.6;
    color: #333;
    max-width: 1200px;
    margin: 0 auto;
    padding: 20px;
}

details.expandable-section {
    margin: 10px 0;
    padding: 5px;
    border-radius: 4px;
}

details.expandable-section summary {
    cursor: pointer;
    padding: 8px;
    margin: -5px;
    border-radius: 4px;
    list-style: none;
}

details.expandable-section summary::-webkit-details-marker {
    display: none;
}

details.expandable-section summary::before {
    content: "▶";
    display: inline-block;
    margin-right: 8px;
    transition: transform 0.2s;
}

details.expandable-section[open] > summary::before {
    transform: rotate(90deg);
}

table {
    width: 100%;
    border-collapse: collapse;
    margin: 15px 0;
}

th, td {
    border: 1px solid #ddd;
    padding: 8px;
    text-align: left;
}

th {
    background-color: #f5f5f5;
}

code {
    background-color: #f5f5f5;
    padding: 2px 4px;
    border-radius: 3px;
    font-family: monospace;
}

.loop-info {
    display: inline-block;
    position: relative;
    color: #666;
    font-size: 0.9em;
    margin-left: 8px;
    cursor: help;
}

.loop-info::after {
    content: "ℹ️";
    margin-left: 4px;
}

.loop-info .tooltip {
    visibility: hidden;
    position: absolute;
    z-index: 1;
    bottom: 125%;
    left: 50%;
    transform: translateX(-50%);
    width: 300px;
    background-color: #333;
    color: white;
    text-align: center;
    padding: 8px;
    border-radius: 6px;
    opacity: 0;
    transition: opacity 0.3s;
}

.loop-info:hover .tooltip {
    visibility: visible;
    opacity: 1;
}

table {
    width: 100%;
    border-collapse: collapse;
    margin: 15px 0;
}

th, td {
    border: 1px solid #ddd;
    padding: 8px;
    text-align: left;
}

th {
    background-color: #f5f5f5;
}

pre {
    background-color: #f8f8f8;
    padding: 15px;
    border-radius: 6px;
    overflow-x: auto;
    margin: 15px 0;
}

code {
    font-family: monospace;
    font-size: 14px;
    line-height: 1.5;
}

pre code {
    font-family: monospace;
    font-size: 14px;
    line-height: 1.5;
    white-space: pre-wrap;
    word-wrap: break-word;
    color: #333;
}

code strong {
    background-color: #fff3b8;
    padding: 2px 4px;
    border-radius: 3px;
    font-weight: bold;
}
</style>
# Django Template Variables Documentation

## Table of Contents
- [absolute_url](#absolute_url)
- [approved_by](#approved_by)
- [appt](#appt)
- [attention](#attention)
- [base_url](#base_url)
- [bounce_address](#bounce_address)
- [cc_list](#cc_list)
- [changerequest](#changerequest)
- [chat_message](#chat_message)
- [client](#client)
- [config](#config)
- [contractor](#contractor)
- [contractor_contact](#contractor_contact)
- [contractor_login_url](#contractor_login_url)
- [csv_url](#csv_url)
- [custom_message](#custom_message)
- [customer](#customer)
- [declined_by](#declined_by)
- [description](#description)
- [email](#email)
- [end_date](#end_date)
- [exception](#exception)
- [failure_datetime](#failure_datetime)
- [failure_reason](#failure_reason)
- [formatted_reason](#formatted_reason)
- [formatted_timestamp](#formatted_timestamp)
- [formresponse](#formresponse)
- [from](#from)
- [inv](#inv)
- [invoice](#invoice)
- [item](#item)
- [lead_engineer](#lead_engineer)
- [line](#line)
- [logbook](#logbook)
- [login_url](#login_url)
- [message](#message)
- [name](#name)
- [no_of_assets](#no_of_assets)
- [payload](#payload)
- [promptset](#promptset)
- [property](#property)
- [purchaseorder](#purchaseorder)
- [quote](#quote)
- [rectification](#rectification)
- [ref_no](#ref_no)
- [rejection_reason](#rejection_reason)
- [remark](#remark)
- [report](#report)
- [request_user](#request_user)
- [retry_link](#retry_link)
- [routineserviceleveltype](#routineserviceleveltype)
- [rslt](#rslt)
- [scope_of_works](#scope_of_works)
- [sender](#sender)
- [servicequote](#servicequote)
- [servicetask](#servicetask)
- [signoff](#signoff)
- [signoffitem](#signoffitem)
- [signoffproperties](#signoffproperties)
- [signoffproperty](#signoffproperty)
- [start_date](#start_date)
- [subject](#subject)
- [task](#task)
- [task_origin_defectquote](#task_origin_defectquote)
- [task_quote](#task_quote)
- [tasksession](#tasksession)
- [template](#template)
- [title](#title)
- [to_list](#to_list)
- [url](#url)

---

## absolute_url

<details class="expandable-section">
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details>
<summary><strong>Usage Examples</strong></summary>

```django
{% raw %}
&lt;span class="variable-highlight"&gt;{{ rectification.rejection_reason|markdowner }}&lt;/span&gt;
&lt;p&gt;Access the rectification to provide updated information:&lt;/p&gt;
&lt;p&gt;&lt;a href="&lt;span class="variable-highlight"&gt;{{ base_url }}&lt;/span&gt;&lt;span class="variable-highlight"&gt;{{ absolute_url }}&lt;/span&gt;"&gt;&lt;span class="variable-highlight"&gt;{{ base_url }}&lt;/span&gt;&lt;span class="variable-highlight"&gt;{{ absolute_url }}&lt;/span&gt;&lt;/a&gt;&lt;/p&gt;
{% endblock %}
{% extends 'email.html' %}
{% endraw %}
```

</details>

---

## approved_by

<details class="expandable-section">
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details>
<summary><strong>Usage Examples</strong></summary>

```django
{% raw %}
&lt;/p&gt;
&lt;p&gt;
The service quote for &lt;span class="variable-highlight"&gt;{{ property }}&lt;/span&gt; was approved by &lt;span class="variable-highlight"&gt;{{ approved_by }}&lt;/span&gt;.
&lt;/p&gt;
&lt;p&gt;
{% endraw %}
```

</details>

---

## appt
<div class="loop-info">Loop Iterator<span class="tooltip">This variable represents a single item from a list or collection being looped over.</span></div>

<details class="expandable-section">
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details class="expandable-section">
<summary><strong>Properties</strong></summary>


| Property | Example Value |
|----------|---------------|
| `scheduled_start` | `{{appt.scheduled_start}}` |
| `task.authorisation_ref` | `{{appt.task.authorisation_ref}}` |
| `task.description` | `{{appt.task.description}}` |
| `task.name` | `{{appt.task.name}}` |
| `task.property.name` | `{{appt.task.property.name}}` |
| `task.ref` | `{{appt.task.ref}}` |
| `task.scope_of_works` | `{{ appt.task.scope_of_works }}` |
| `technicians.first` | `{{appt.technicians.first}}` |

</details>

<details>
<summary><strong>Usage Examples</strong></summary>

```django
{% raw %}
{% timezone tmz %}
&lt;tr&gt;
&lt;th style="..." scope="row" colspan="4"&gt;&lt;span class="variable-highlight"&gt;{{appt.scheduled_start}}&lt;/span&gt;&lt;/th&gt;
&lt;td style="..."&gt;&lt;span class="variable-highlight"&gt;{{appt.task.description}}&lt;/span&gt;&lt;/td&gt;
&lt;td style="..."&gt;&lt;span class="variable-highlight"&gt;{{appt.task.property.name}}&lt;/span&gt;&lt;/td&gt;
{% endraw %}
```

```django
{% raw %}
&lt;tr&gt;
&lt;th style="..." scope="row" colspan="4"&gt;&lt;span class="variable-highlight"&gt;{{appt.scheduled_start}}&lt;/span&gt;&lt;/th&gt;
&lt;td style="..."&gt;&lt;span class="variable-highlight"&gt;{{appt.task.description}}&lt;/span&gt;&lt;/td&gt;
&lt;td style="..."&gt;&lt;span class="variable-highlight"&gt;{{appt.task.property.name}}&lt;/span&gt;&lt;/td&gt;
&lt;td style="..."&gt;&lt;span class="variable-highlight"&gt;{{appt.task.scope_of_works}}&lt;/span&gt;&lt;/td&gt;
{% endraw %}
```

```django
{% raw %}
&lt;th style="..." scope="row" colspan="4"&gt;&lt;span class="variable-highlight"&gt;{{appt.scheduled_start}}&lt;/span&gt;&lt;/th&gt;
&lt;td style="..."&gt;&lt;span class="variable-highlight"&gt;{{appt.task.description}}&lt;/span&gt;&lt;/td&gt;
&lt;td style="..."&gt;&lt;span class="variable-highlight"&gt;{{appt.task.property.name}}&lt;/span&gt;&lt;/td&gt;
&lt;td style="..."&gt;&lt;span class="variable-highlight"&gt;{{appt.task.scope_of_works}}&lt;/span&gt;&lt;/td&gt;
&lt;td style="..."&gt;&lt;span class="variable-highlight"&gt;{{appt.task.authorisation_ref}}&lt;/span&gt;&lt;/td&gt;
{% endraw %}
```

</details>

---

## attention

**Default values:** `Manager`, `manager`

<details class="expandable-section">
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details class="expandable-section">
<summary><strong>Filters Used</strong></summary>

- `default (arg: "Manager")`
- `default (arg: "manager")`

</details>

<details>
<summary><strong>Usage Examples</strong></summary>

```django
{% raw %}
&lt;td style="..."&gt;
&lt;div style="..."&gt;
&lt;p style="..."&gt;Dear &lt;span class="variable-highlight"&gt;{{ attention }}&lt;/span&gt;,&lt;/p&gt;
&lt;p&gt;Please be advised we will need access to complete the following:&lt;/p&gt;
&lt;table style="..."&gt;
{% endraw %}
```

```django
{% raw %}
&lt;/table&gt;
{% endblock %}
&lt;p&gt;Dear &lt;span class="variable-highlight"&gt;{{ attention }}&lt;/span&gt;,&lt;/p&gt;
&lt;p&gt;Please find attached your defect quote for &lt;span class="variable-highlight"&gt;{{ property.name }}&lt;/span&gt;.&lt;/p&gt;
&lt;p&gt;To view and approve this quote online, visit:&lt;/p&gt;
{% endraw %}
```

```django
{% raw %}
&lt;p&gt;Regards,&lt;br /&gt;
&lt;span class="variable-highlight"&gt;{{ config.SITE_ORGANISATION }}&lt;/span&gt;&lt;/p&gt;
&lt;p&gt;Dear &lt;span class="variable-highlight"&gt;{{ attention|default:"manager" }}&lt;/span&gt;,&lt;/p&gt;
&lt;p&gt;Please find attached your documents for services recently carried out at &lt;span class="variable-highlight"&gt;{{ property.name }}&lt;/span&gt;.&lt;/p&gt;
{% if invoice %}
{% endraw %}
```

</details>

---

## base_url

<details class="expandable-section">
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details>
<summary><strong>Usage Examples</strong></summary>

```django
{% raw %}
&lt;p&gt;Please find attached your defect quote for &lt;span class="variable-highlight"&gt;{{ property.name }}&lt;/span&gt;.&lt;/p&gt;
&lt;p&gt;To view and approve this quote online, visit:&lt;/p&gt;
&lt;p&gt;&lt;a href="&lt;span class="variable-highlight"&gt;{{ base_url }}&lt;/span&gt;&lt;span class="variable-highlight"&gt;{{ quote.get_uuid_approval_url }}&lt;/span&gt;"&gt;&lt;span class="variable-highlight"&gt;{{ base_url }}&lt;/span&gt;&lt;span class="variable-highlight"&gt;{{ quote.get_uuid_approval_url }}&lt;/span&gt;&lt;/a&gt;&lt;/p&gt;
&lt;p&gt;We value your opinion, please contact us with any comments you may have.&lt;/p&gt;
&lt;p&gt;Regards,&lt;br /&gt;
{% endraw %}
```

```django
{% raw %}
&lt;ul&gt;
{% for quote in defectquotes %}
&lt;li&gt;Reference: &lt;span class="variable-highlight"&gt;{{ quote.ref }}&lt;/span&gt;&lt;a href="&lt;span class="variable-highlight"&gt;{{ base_url }}&lt;/span&gt;&lt;span class="variable-highlight"&gt;{{ quote.get_uuid_approval_url }}&lt;/span&gt;"&gt; (approve online)&lt;/a&gt;&lt;/li&gt;
{% endfor %}
&lt;/ul&gt;
{% endraw %}
```

```django
{% raw %}
&lt;p&gt;
Please go to this URL to set your password and start using Uptick:
&lt;span class="variable-highlight"&gt;{{ base_url }}&lt;/span&gt;{% url 'password_reset_confirm' uidb64=uid token=token %}
&lt;/p&gt;
{% if account.license == "FIELD" %}
{% endraw %}
```

</details>

---

## bounce_address

<details class="expandable-section">
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details>
<summary><strong>Usage Examples</strong></summary>

```django
{% raw %}
&lt;p&gt;
Bounce info:&lt;br /&gt;
Address: &lt;span class="variable-highlight"&gt;{{ bounce_address }}&lt;/span&gt;&lt;br /&gt;
Bounce Reason: &lt;span class="variable-highlight"&gt;{{ formatted_reason }}&lt;/span&gt;&lt;br /&gt;
Email Subject &lt;span class="variable-highlight"&gt;{{ subject }}&lt;/span&gt;&lt;br /&gt;
{% endraw %}
```

</details>

---

## cc_list

<details class="expandable-section">
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details>
<summary><strong>Usage Examples</strong></summary>

```django
{% raw %}
Sent: &lt;span class="variable-highlight"&gt;{{ failure_datetime }}&lt;/span&gt;&lt;br /&gt;
To: &lt;span class="variable-highlight"&gt;{{ to_list }}&lt;/span&gt;&lt;br /&gt;
CC: &lt;span class="variable-highlight"&gt;{{ cc_list }}&lt;/span&gt;&lt;br /&gt;
Subject &lt;span class="variable-highlight"&gt;{{ subject }}&lt;/span&gt;&lt;br /&gt;
&lt;/p&gt;
{% endraw %}
```

</details>

---

## changerequest

<details class="expandable-section">
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details class="expandable-section">
<summary><strong>Properties</strong></summary>


| Property | Example Value |
|----------|---------------|
| `get_absolute_url` | `{{ changerequest.get_absolute_url }}` |
| `ref` | `{{ changerequest.ref }}` |
| `status` | `{{ changerequest.status }}` |

</details>

<details>
<summary><strong>Usage Examples</strong></summary>

```django
{% raw %}
&lt;span class="variable-highlight"&gt;{{ config.SITE_ORGANISATION }}&lt;/span&gt;&lt;/p&gt;
{% if status == 'DRAFT' %}
&lt;p&gt;Template change request &lt;span class="variable-highlight"&gt;{{ changerequest.ref }}&lt;/span&gt; has been created for &lt;span class="variable-highlight"&gt;{{ customer }}&lt;/span&gt;.&lt;/p&gt;
{% elif  status == 'REQUESTED' %}
&lt;p&gt;&lt;span class="variable-highlight"&gt;{{ sender.name }}&lt;/span&gt; submitted feedback for Template change request &lt;span class="variable-highlight"&gt;{{ changerequest.ref }}&lt;/span&gt;.&lt;/p&gt;
{% endraw %}
```

```django
{% raw %}
&lt;p&gt;Template change request &lt;span class="variable-highlight"&gt;{{ changerequest.ref }}&lt;/span&gt; has been created for &lt;span class="variable-highlight"&gt;{{ customer }}&lt;/span&gt;.&lt;/p&gt;
{% elif  status == 'REQUESTED' %}
&lt;p&gt;&lt;span class="variable-highlight"&gt;{{ sender.name }}&lt;/span&gt; submitted feedback for Template change request &lt;span class="variable-highlight"&gt;{{ changerequest.ref }}&lt;/span&gt;.&lt;/p&gt;
{% else %}
&lt;p&gt;Template change request &lt;span class="variable-highlight"&gt;{{ changerequest.ref }}&lt;/span&gt; has been approved. Our team will be in contact once completed.&lt;/p&gt;
{% endraw %}
```

```django
{% raw %}
&lt;p&gt;&lt;span class="variable-highlight"&gt;{{ sender.name }}&lt;/span&gt; submitted feedback for Template change request &lt;span class="variable-highlight"&gt;{{ changerequest.ref }}&lt;/span&gt;.&lt;/p&gt;
{% else %}
&lt;p&gt;Template change request &lt;span class="variable-highlight"&gt;{{ changerequest.ref }}&lt;/span&gt; has been approved. Our team will be in contact once completed.&lt;/p&gt;
{% endif %}
&lt;p&gt;
{% endraw %}
```

</details>

---

## chat_message

<details class="expandable-section">
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details class="expandable-section">
<summary><strong>Properties</strong></summary>


| Property | Example Value |
|----------|---------------|
| `text` | `{{ chat_message.text }}` |

</details>

<details>
<summary><strong>Usage Examples</strong></summary>

```django
{% raw %}
&lt;/p&gt;
&lt;p&gt;A new message from &lt;span class="variable-highlight"&gt;{{ from }}&lt;/span&gt; is waiting for you:&lt;/p&gt;
&lt;p&gt;&lt;span class="variable-highlight"&gt;{{ chat_message.text }}&lt;/span&gt;&lt;/p&gt;
&lt;p&gt;&lt;span class="variable-highlight"&gt;{{ base_url }}&lt;/span&gt;&lt;span class="variable-highlight"&gt;{{ url }}&lt;/span&gt;&lt;/p&gt;
&lt;p&gt;Regards, &lt;br/&gt;
{% endraw %}
```

```django
{% raw %}
{% endblock %}
&lt;p&gt;A new message from &lt;span class="variable-highlight"&gt;{{ from }}&lt;/span&gt; is waiting for you:&lt;/p&gt;
&lt;p&gt;&lt;span class="variable-highlight"&gt;{{ chat_message.text }}&lt;/span&gt;&lt;/p&gt;
&lt;p&gt;&lt;span class="variable-highlight"&gt;{{ base_url }}&lt;/span&gt;&lt;span class="variable-highlight"&gt;{{ url }}&lt;/span&gt;&lt;/p&gt;
&lt;p&gt;Regards, &lt;br/&gt;
{% endraw %}
```

</details>

---

## client

<details class="expandable-section">
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details class="expandable-section">
<summary><strong>Properties</strong></summary>


| Property | Example Value |
|----------|---------------|
| `primary_contact.name` | `{{ client.primary_contact.name }}` |

</details>

<details>
<summary><strong>Usage Examples</strong></summary>

```django
{% raw %}
&lt;p&gt;If the form&lt;span class="variable-highlight"&gt;{{ signoffproperties|pluralize }}&lt;/span&gt; on the attached link &lt;span class="variable-highlight"&gt;{{ signoffproperties|pluralize:"is,are" }}&lt;/span&gt; not submitted and there is no proof on site that the Essential Safety Measures are being serviced, &lt;span class="variable-highlight"&gt;{{ signoffproperties|pluralize:"a," }}&lt;/span&gt; Non-Compliant Building Report&lt;span class="variable-highlight"&gt;{{ signoffproperties|pluralize }}&lt;/span&gt; will be issued.&lt;/p&gt;
{% endblock %}
&lt;p&gt;Dear &lt;span class="variable-highlight"&gt;{{ client.primary_contact.name }}&lt;/span&gt;,&lt;/p&gt;
&lt;p&gt;This email is in regards to your property &lt;span class="variable-highlight"&gt;{{ property.ref }}&lt;/span&gt; &lt;span class="variable-highlight"&gt;{{ property.name }}&lt;/span&gt; &lt;span class="variable-highlight"&gt;{{ property.client_ref }}&lt;/span&gt;.&lt;/p&gt;
&lt;p&gt;We have received notification from &lt;span class="variable-highlight"&gt;{{ contractor.name }}&lt;/span&gt; that they are no longer engaged to maintain the following items:&lt;/p&gt;
{% endraw %}
```

```django
{% raw %}
&lt;div&gt;&lt;span class="variable-highlight"&gt;{{ servicequote.created|date:"jS F Y" }}&lt;/span&gt;&lt;/div&gt;
{% if servicequote.expiry_date %}&lt;div&gt;This quote is valid until &lt;em&gt;&lt;span class="variable-highlight"&gt;{{ servicequote.expiry_date }}&lt;/span&gt;&lt;/em&gt;&lt;/div&gt;{% endif %}
&lt;div&gt;&lt;strong&gt;Attention: &lt;span class="variable-highlight"&gt;{{ client.primary_contact.name }}&lt;/span&gt;&lt;/strong&gt;&lt;/div&gt;
{% if servicequote.scope_of_works %}
&lt;div class="mt-3"&gt;
{% endraw %}
```

</details>

---

## config

<details class="expandable-section">
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details class="expandable-section">
<summary><strong>Properties</strong></summary>


| Property | Example Value |
|----------|---------------|
| `CONTACT_EMAIL` | `{{ config.CONTACT_EMAIL }}` |
| `CONTACT_PHONE` | `{{ config.CONTACT_PHONE }}` |
| `SITE_ORGANISATION` | `{{config.SITE_ORGANISATION}}` |

</details>

<details>
<summary><strong>Usage Examples</strong></summary>

```django
{% raw %}
&lt;p&gt;&lt;span class="variable-highlight"&gt;{{request_user.email}}&lt;/span&gt;&lt;/p&gt;
&lt;p&gt;
&lt;span class="variable-highlight"&gt;{{ config.CONTACT_PHONE }}&lt;/span&gt; &lt;br /&gt;
&lt;span class="variable-highlight"&gt;{{ config.SITE_ORGANISATION }}&lt;/span&gt;
&lt;/p&gt;
{% endraw %}
```

```django
{% raw %}
&lt;p&gt;
&lt;span class="variable-highlight"&gt;{{ config.CONTACT_PHONE }}&lt;/span&gt; &lt;br /&gt;
&lt;span class="variable-highlight"&gt;{{ config.SITE_ORGANISATION }}&lt;/span&gt;
&lt;/p&gt;
&lt;/div&gt;
{% endraw %}
```

```django
{% raw %}
&lt;p&gt;We value your opinion, please contact us with any comments you may have.&lt;/p&gt;
&lt;p&gt;Regards,&lt;br /&gt;
&lt;span class="variable-highlight"&gt;{{ config.SITE_ORGANISATION }}&lt;/span&gt;&lt;/p&gt;
&lt;p&gt;Dear &lt;span class="variable-highlight"&gt;{{ attention|default:"manager" }}&lt;/span&gt;,&lt;/p&gt;
&lt;p&gt;Please find attached your documents for services recently carried out at &lt;span class="variable-highlight"&gt;{{ property.name }}&lt;/span&gt;.&lt;/p&gt;
{% endraw %}
```

</details>

---

## contractor

<details class="expandable-section">
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details class="expandable-section">
<summary><strong>Properties</strong></summary>


| Property | Example Value |
|----------|---------------|
| `account` | `{{ contractor.account }}` |
| `name` | `{{ contractor.name }}` |

</details>

<details>
<summary><strong>Usage Examples</strong></summary>

```django
{% raw %}
&lt;span class="variable-highlight"&gt;{{ config.SITE_ORGANISATION }}&lt;/span&gt;&lt;/p&gt;
{% endblock %}
&lt;p&gt;Dear &lt;span class="variable-highlight"&gt;{{ contractor }}&lt;/span&gt;,&lt;/p&gt;
&lt;p&gt;You have been assigned the following tasks:&lt;/p&gt;
{% for task in tasks %}
{% endraw %}
```

```django
{% raw %}
&lt;p&gt;You can provide your field technicians with this link which will enable them to complete the task via their smart phone (apple or android) without needing to install an app.&lt;/p&gt;
&lt;p&gt;Thanks&lt;/p&gt;
&lt;p&gt;The contractor &lt;span class="variable-highlight"&gt;{{ contractor }}&lt;/span&gt; has rejected the task assigned to him for the following reason: &lt;span class="variable-highlight"&gt;{{ rejection_reason }}&lt;/span&gt;&lt;/p&gt;
&lt;p&gt;
The task that was assigned was:&lt;br&gt;
{% endraw %}
```

```django
{% raw %}
&lt;/p&gt;
&lt;p&gt;Thanks&lt;/p&gt;
&lt;p&gt;Dear &lt;span class="variable-highlight"&gt;{{ contractor }}&lt;/span&gt;,&lt;/p&gt;
&lt;p&gt;Please be advised that the following task has been cancelled:&lt;/p&gt;
&lt;ul&gt;
{% endraw %}
```

</details>

---

## contractor_contact

<details class="expandable-section">
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details class="expandable-section">
<summary><strong>Properties</strong></summary>


| Property | Example Value |
|----------|---------------|
| `name` | `{{ contractor_contact.name }}` |

</details>

<details>
<summary><strong>Usage Examples</strong></summary>

```django
{% raw %}
&lt;p&gt;Regards,&lt;br/&gt;
&lt;span class="variable-highlight"&gt;{{ config.SITE_ORGANISATION }}&lt;/span&gt;&lt;/p&gt;
&lt;p&gt;Dear &lt;span class="variable-highlight"&gt;{{ contractor_contact }}&lt;/span&gt;,&lt;/p&gt;
&lt;p&gt;Please be advised that the following task has been cancelled:&lt;/p&gt;
&lt;ul&gt;
{% endraw %}
```

```django
{% raw %}
&lt;span class="variable-highlight"&gt;{{ config.SITE_ORGANISATION }}&lt;/span&gt;
&lt;/p&gt;
&lt;p&gt;Dear &lt;span class="variable-highlight"&gt;{{ contractor_contact.name }}&lt;/span&gt;,&lt;/p&gt;
&lt;p&gt;You have been assigned a task:&lt;/p&gt;
&lt;p&gt;Task &lt;span class="variable-highlight"&gt;{{ task.ref }}&lt;/span&gt;&lt;/p&gt;
{% endraw %}
```

```django
{% raw %}
&lt;/p&gt;
&lt;p&gt;Thanks&lt;/p&gt;
&lt;p&gt;Dear &lt;span class="variable-highlight"&gt;{{ contractor_contact.name }}&lt;/span&gt;,&lt;/p&gt;
&lt;p&gt;You have been assigned the following tasks:&lt;/p&gt;
{% for task in tasks %}
{% endraw %}
```

</details>

---

## contractor_login_url

<details class="expandable-section">
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details>
<summary><strong>Usage Examples</strong></summary>

```django
{% raw %}
&lt;p&gt;
Please sign in the contractor portal using the link below to view a list of any outstanding tasks:&lt;br&gt;
&lt;a href="&lt;span class="variable-highlight"&gt;{{ contractor_login_url }}&lt;/span&gt;"&gt;&lt;span class="variable-highlight"&gt;{{ contractor_login_url }}&lt;/span&gt;&lt;/a&gt;
&lt;/p&gt;
&lt;p&gt;You can provide your field technicians with this link which will enable them to complete the task via their smart phone (apple or android) without needing to install an app.&lt;/p&gt;
{% endraw %}
```

```django
{% raw %}
&lt;p&gt;
Please visit the task dashboard on Uptick:&lt;br&gt;
&lt;a href="&lt;span class="variable-highlight"&gt;{{ contractor_login_url }}&lt;/span&gt;"&gt;&lt;span class="variable-highlight"&gt;{{ contractor_login_url }}&lt;/span&gt;&lt;/a&gt;&lt;br&gt;
for more details.
&lt;/p&gt;
{% endraw %}
```

```django
{% raw %}
&lt;p&gt;&lt;span class="variable-highlight"&gt;{{ task.address }}&lt;/span&gt;&lt;/p&gt;
&lt;p&gt;Please sign into the contractor portal using the link below to view your outstanding tasks:&lt;br&gt;
&lt;a href="&lt;span class="variable-highlight"&gt;{{ contractor_login_url }}&lt;/span&gt;"&gt;&lt;span class="variable-highlight"&gt;{{ contractor_login_url }}&lt;/span&gt;&lt;/a&gt;
&lt;/p&gt;
&lt;p&gt;Thanks&lt;/p&gt;
{% endraw %}
```

</details>

---

## csv_url

<details class="expandable-section">
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details>
<summary><strong>Usage Examples</strong></summary>

```django
{% raw %}
&lt;p&gt;Your custom report, &lt;span class="variable-highlight"&gt;{{ name }}&lt;/span&gt;, has been generated.&lt;/p&gt;
&lt;p&gt;&lt;span class="variable-highlight"&gt;{{ description }}&lt;/span&gt;&lt;/p&gt;
&lt;p&gt;To download, &lt;a href="&lt;span class="variable-highlight"&gt;{{ csv_url }}&lt;/span&gt;"&gt;please click here&lt;/a&gt;.&lt;/p&gt;
{% endblock %}
&lt;p&gt;Dear &lt;span class="variable-highlight"&gt;{{ attention }}&lt;/span&gt;,&lt;/p&gt;
{% endraw %}
```

</details>

---

## custom_message

<details class="expandable-section">
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details>
<summary><strong>Usage Examples</strong></summary>

```django
{% raw %}
{% if custom_message %}
&lt;p&gt;
&lt;span class="variable-highlight"&gt;{{ custom_message }}&lt;/span&gt;
&lt;/p&gt;
{% endif %}
{% endraw %}
```

</details>

---

## customer

<details class="expandable-section">
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details>
<summary><strong>Usage Examples</strong></summary>

```django
{% raw %}
&lt;span class="variable-highlight"&gt;{{ config.SITE_ORGANISATION }}&lt;/span&gt;&lt;/p&gt;
{% if status == 'DRAFT' %}
&lt;p&gt;Template change request &lt;span class="variable-highlight"&gt;{{ changerequest.ref }}&lt;/span&gt; has been created for &lt;span class="variable-highlight"&gt;{{ customer }}&lt;/span&gt;.&lt;/p&gt;
{% elif  status == 'REQUESTED' %}
&lt;p&gt;&lt;span class="variable-highlight"&gt;{{ sender.name }}&lt;/span&gt; submitted feedback for Template change request &lt;span class="variable-highlight"&gt;{{ changerequest.ref }}&lt;/span&gt;.&lt;/p&gt;
{% endraw %}
```

</details>

---

## declined_by

<details class="expandable-section">
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details>
<summary><strong>Usage Examples</strong></summary>

```django
{% raw %}
&lt;/p&gt;
&lt;p&gt;
The service quote for &lt;span class="variable-highlight"&gt;{{ property }}&lt;/span&gt; was declined by &lt;span class="variable-highlight"&gt;{{ declined_by }}&lt;/span&gt;.
&lt;/p&gt;
&lt;p&gt;
{% endraw %}
```

</details>

---

## description

<details class="expandable-section">
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details>
<summary><strong>Usage Examples</strong></summary>

```django
{% raw %}
{% block content %}
&lt;p&gt;Your custom report, &lt;span class="variable-highlight"&gt;{{ name }}&lt;/span&gt;, has been generated.&lt;/p&gt;
&lt;p&gt;&lt;span class="variable-highlight"&gt;{{ description }}&lt;/span&gt;&lt;/p&gt;
&lt;p&gt;To download, &lt;a href="&lt;span class="variable-highlight"&gt;{{ csv_url }}&lt;/span&gt;"&gt;please click here&lt;/a&gt;.&lt;/p&gt;
{% endblock %}
{% endraw %}
```

</details>

---

## email
<div class="loop-info">Loop Iterator<span class="tooltip">This variable represents a single item from a list or collection being looped over.</span></div>

<details class="expandable-section">
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details>
<summary><strong>Usage Examples</strong></summary>

```django
{% raw %}
{% for email in quote_email_lookup|getvalue:quote %}
{% if email != recipient %}
&lt;li&gt;&lt;span class="variable-highlight"&gt;{{email}}&lt;/span&gt;&lt;/li&gt;
{% endif %}
{% endfor %}
{% endraw %}
```

</details>

---

## end_date

<details class="expandable-section">
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details>
<summary><strong>Usage Examples</strong></summary>

```django
{% raw %}
&lt;td style="..."&gt;&lt;span class="variable-highlight"&gt;{{start_date}}&lt;/span&gt;&lt;/td&gt;
&lt;td style="..."&gt;END DATE&lt;/td&gt;
&lt;td style="..."&gt;&lt;span class="variable-highlight"&gt;{{end_date}}&lt;/span&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
{% endraw %}
```

</details>

---

## exception

<details class="expandable-section">
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details>
<summary><strong>Usage Examples</strong></summary>

```django
{% raw %}
&lt;/p&gt;
&lt;h3&gt;Error&lt;/h3&gt;
&lt;code&gt;&lt;span class="variable-highlight"&gt;{{ exception }}&lt;/span&gt;&lt;/code&gt;
&lt;p&gt;
An email failed to send from Uptick! This is sometimes due to an invalid email, but more details below.
{% endraw %}
```

</details>

---

## failure_datetime

<details class="expandable-section">
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details>
<summary><strong>Usage Examples</strong></summary>

```django
{% raw %}
&lt;p&gt;
Email info:&lt;br /&gt;
Sent: &lt;span class="variable-highlight"&gt;{{ failure_datetime }}&lt;/span&gt;&lt;br /&gt;
To: &lt;span class="variable-highlight"&gt;{{ to_list }}&lt;/span&gt;&lt;br /&gt;
CC: &lt;span class="variable-highlight"&gt;{{ cc_list }}&lt;/span&gt;&lt;br /&gt;
{% endraw %}
```

</details>

---

## failure_reason

<details class="expandable-section">
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details>
<summary><strong>Usage Examples</strong></summary>

```django
{% raw %}
An email failed to send from Uptick! This is sometimes due to an invalid email, but more details below.
&lt;br /&gt;
&lt;span class="variable-highlight"&gt;{{ failure_reason }}&lt;/span&gt;
&lt;/p&gt;
&lt;p&gt;
{% endraw %}
```

</details>

---

## formatted_reason

<details class="expandable-section">
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details>
<summary><strong>Usage Examples</strong></summary>

```django
{% raw %}
Bounce info:&lt;br /&gt;
Address: &lt;span class="variable-highlight"&gt;{{ bounce_address }}&lt;/span&gt;&lt;br /&gt;
Bounce Reason: &lt;span class="variable-highlight"&gt;{{ formatted_reason }}&lt;/span&gt;&lt;br /&gt;
Email Subject &lt;span class="variable-highlight"&gt;{{ subject }}&lt;/span&gt;&lt;br /&gt;
Email Sent: &lt;span class="variable-highlight"&gt;{{ formatted_timestamp }}&lt;/span&gt;
{% endraw %}
```

</details>

---

## formatted_timestamp

<details class="expandable-section">
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details>
<summary><strong>Usage Examples</strong></summary>

```django
{% raw %}
Bounce Reason: &lt;span class="variable-highlight"&gt;{{ formatted_reason }}&lt;/span&gt;&lt;br /&gt;
Email Subject &lt;span class="variable-highlight"&gt;{{ subject }}&lt;/span&gt;&lt;br /&gt;
Email Sent: &lt;span class="variable-highlight"&gt;{{ formatted_timestamp }}&lt;/span&gt;
&lt;/p&gt;
&lt;p&gt;
{% endraw %}
```

</details>

---

## formresponse
<div class="loop-info">Loop Iterator<span class="tooltip">This variable represents a single item from a list or collection being looped over.</span></div>

<details class="expandable-section">
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details class="expandable-section">
<summary><strong>Properties</strong></summary>


| Property | Example Value |
|----------|---------------|
| `submitter` | `{{ formresponse.submitter }}` |
| `template_version.template.name` | `{{ formresponse.template_version.template.name }}` |

</details>

<details>
<summary><strong>Usage Examples</strong></summary>

```django
{% raw %}
&lt;ul&gt;
{% for formresponse in formresponses %}
&lt;li&gt;&lt;span class="variable-highlight"&gt;{{ formresponse }}&lt;/span&gt;&lt;/li&gt;
{% endfor %}
&lt;/ul&gt;
{% endraw %}
```

```django
{% raw %}
&lt;/p&gt;&lt;p&gt;Dear &lt;span class="variable-highlight"&gt;{{ attention }}&lt;/span&gt;,&lt;/p&gt;
&lt;p&gt;Please find attached a form response regarding work at &lt;span class="variable-highlight"&gt;{{ property.name }}&lt;/span&gt;.&lt;/p&gt;
&lt;p&gt;Form: &lt;span class="variable-highlight"&gt;{{ formresponse.template_version.template.name }}&lt;/span&gt;&lt;/p&gt;
&lt;p&gt;Submitted by: &lt;span class="variable-highlight"&gt;{{ formresponse.submitter }}&lt;/span&gt;&lt;/p&gt;
&lt;p&gt;We value your opinion, please contact us with any comments you may have.&lt;/p&gt;
{% endraw %}
```

```django
{% raw %}
&lt;p&gt;Please find attached a form response regarding work at &lt;span class="variable-highlight"&gt;{{ property.name }}&lt;/span&gt;.&lt;/p&gt;
&lt;p&gt;Form: &lt;span class="variable-highlight"&gt;{{ formresponse.template_version.template.name }}&lt;/span&gt;&lt;/p&gt;
&lt;p&gt;Submitted by: &lt;span class="variable-highlight"&gt;{{ formresponse.submitter }}&lt;/span&gt;&lt;/p&gt;
&lt;p&gt;We value your opinion, please contact us with any comments you may have.&lt;/p&gt;
&lt;p&gt;Regards,&lt;br /&gt;
{% endraw %}
```

</details>

---

## from

<details class="expandable-section">
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details>
<summary><strong>Usage Examples</strong></summary>

```django
{% raw %}
&lt;span class="variable-highlight"&gt;{{ config.SITE_ORGANISATION }}&lt;/span&gt;
&lt;/p&gt;
&lt;p&gt;A new message from &lt;span class="variable-highlight"&gt;{{ from }}&lt;/span&gt; is waiting for you:&lt;/p&gt;
&lt;p&gt;&lt;span class="variable-highlight"&gt;{{ chat_message.text }}&lt;/span&gt;&lt;/p&gt;
&lt;p&gt;&lt;span class="variable-highlight"&gt;{{ base_url }}&lt;/span&gt;&lt;span class="variable-highlight"&gt;{{ url }}&lt;/span&gt;&lt;/p&gt;
{% endraw %}
```

```django
{% raw %}
{% endfor %}
{% endblock %}
&lt;p&gt;A new message from &lt;span class="variable-highlight"&gt;{{ from }}&lt;/span&gt; is waiting for you:&lt;/p&gt;
&lt;p&gt;&lt;span class="variable-highlight"&gt;{{ chat_message.text }}&lt;/span&gt;&lt;/p&gt;
&lt;p&gt;&lt;span class="variable-highlight"&gt;{{ base_url }}&lt;/span&gt;&lt;span class="variable-highlight"&gt;{{ url }}&lt;/span&gt;&lt;/p&gt;
{% endraw %}
```

</details>

---

## inv
<div class="loop-info">Loop Iterator<span class="tooltip">This variable represents a single item from a list or collection being looped over.</span></div>

<details class="expandable-section">
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details class="expandable-section">
<summary><strong>Properties</strong></summary>


| Property | Example Value |
|----------|---------------|
| `number` | `{{ inv.number }}` |
| `ref` | `{{ inv.ref }}` |

</details>

<details>
<summary><strong>Usage Examples</strong></summary>

```django
{% raw %}
&lt;p&gt;This is a reminder that we are waiting for your payment on the following invoices:&lt;br&gt;
{% for inv in invoices %}&lt;br&gt;
Number: &lt;span class="variable-highlight"&gt;{{ inv.number }}&lt;/span&gt;&lt;br&gt;
Reference: &lt;span class="variable-highlight"&gt;{{ inv.ref }}&lt;/span&gt;&lt;br&gt;
Due: &lt;span class="variable-highlight"&gt;{{ inv.due_date|date:"jS F Y" }}&lt;/span&gt;&lt;br&gt;
{% endraw %}
```

```django
{% raw %}
{% for inv in invoices %}&lt;br&gt;
Number: &lt;span class="variable-highlight"&gt;{{ inv.number }}&lt;/span&gt;&lt;br&gt;
Reference: &lt;span class="variable-highlight"&gt;{{ inv.ref }}&lt;/span&gt;&lt;br&gt;
Due: &lt;span class="variable-highlight"&gt;{{ inv.due_date|date:"jS F Y" }}&lt;/span&gt;&lt;br&gt;
{% endfor %}
{% endraw %}
```

</details>

---

## invoice

<details class="expandable-section">
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details class="expandable-section">
<summary><strong>Properties</strong></summary>


| Property | Example Value |
|----------|---------------|
| `ref` | `{{ invoice.ref }}` |

</details>

<details>
<summary><strong>Usage Examples</strong></summary>

```django
{% raw %}
&lt;p&gt;Your invoice:&lt;/p&gt;
&lt;ul&gt;
&lt;li&gt;&lt;span class="variable-highlight"&gt;{{ invoice.number|default:"[[ invoice_number ]]" }}&lt;/span&gt; {% if invoice.ref %}(&lt;span class="variable-highlight"&gt;{{ invoice.ref }}&lt;/span&gt;){% endif %}&lt;/li&gt;
&lt;/ul&gt;
{% endif %}
{% endraw %}
```

</details>

---

## item
<div class="loop-info">Loop Iterator<span class="tooltip">This variable represents a single item from a list or collection being looped over.</span></div>

<details class="expandable-section">
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details class="expandable-section">
<summary><strong>Properties</strong></summary>


| Property | Example Value |
|----------|---------------|
| `label` | `{{ item.label }}` |

</details>

<details>
<summary><strong>Usage Examples</strong></summary>

```django
{% raw %}
&lt;ul&gt;
{% for item in items %}
&lt;li&gt;&lt;span class="variable-highlight"&gt;{{ item.label }}&lt;/span&gt;&lt;/li&gt;
{% endfor %}
&lt;/ul&gt;
{% endraw %}
```

</details>

---

## lead_engineer

<details class="expandable-section">
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details>
<summary><strong>Usage Examples</strong></summary>

```django
{% raw %}
&lt;tr&gt;
&lt;td style="..."&gt;LEAD ENGINEER&lt;/td&gt;
&lt;td style="..." colspan="3"&gt;&lt;span class="variable-highlight"&gt;{{lead_engineer}}&lt;/span&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
{% endraw %}
```

</details>

---

## line
<div class="loop-info">Loop Iterator<span class="tooltip">This variable represents a single item from a list or collection being looped over.</span></div>

<details class="expandable-section">
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details class="expandable-section">
<summary><strong>Properties</strong></summary>


| Property | Example Value |
|----------|---------------|
| `annual_subtotal` | `{{ line.annual_subtotal\|currency }}` |
| `product.name` | `{{ line.product.name }}` |
| `quantity` | `{{ line.quantity\|floatformat:2 }}` |
| `routineservicetype.name` | `{{ line.routineservicetype.name }}` |
| `site_price` | `{{ line.site_price\|currency }}` |
| `subtotal` | `{{ line.subtotal\|currency }}` |
| `unit_price` | `{{ line.unit_price\|currency }}` |

</details>

<details class="expandable-section">
<summary><strong>Filters Used</strong></summary>

- `currency`
- `floatformat (arg: 2)`

</details>

<details>
<summary><strong>Usage Examples</strong></summary>

```django
{% raw %}
&lt;tr class="keep-together"&gt;
&lt;td&gt;
&lt;div&gt;&lt;span class="variable-highlight"&gt;{{ line.product.name }}&lt;/span&gt;&lt;/div&gt;
&lt;div class="text-muted"&gt;&lt;span class="variable-highlight"&gt;{{ line.description|default:'-' }}&lt;/span&gt;&lt;/div&gt;
&lt;/td&gt;
{% endraw %}
```

```django
{% raw %}
&lt;div class="text-muted"&gt;&lt;span class="variable-highlight"&gt;{{ line.description|default:'-' }}&lt;/span&gt;&lt;/div&gt;
&lt;/td&gt;
&lt;td class="text-right"&gt;&lt;span class="variable-highlight"&gt;{{ line.quantity|floatformat:2 }}&lt;/span&gt;&lt;/td&gt;
&lt;td class="text-right"&gt;&lt;span class="variable-highlight"&gt;{{ line.unit_price|currency }}&lt;/span&gt;&lt;/td&gt;
&lt;td class="text-right"&gt;&lt;span class="variable-highlight"&gt;{{ line.subtotal|currency }}&lt;/span&gt;&lt;/td&gt;
{% endraw %}
```

```django
{% raw %}
&lt;/td&gt;
&lt;td class="text-right"&gt;&lt;span class="variable-highlight"&gt;{{ line.quantity|floatformat:2 }}&lt;/span&gt;&lt;/td&gt;
&lt;td class="text-right"&gt;&lt;span class="variable-highlight"&gt;{{ line.unit_price|currency }}&lt;/span&gt;&lt;/td&gt;
&lt;td class="text-right"&gt;&lt;span class="variable-highlight"&gt;{{ line.subtotal|currency }}&lt;/span&gt;&lt;/td&gt;
&lt;/tr&gt;
{% endraw %}
```

</details>

---

## logbook
<div class="loop-info">Loop Iterator<span class="tooltip">This variable represents a single item from a list or collection being looped over.</span></div>

<details class="expandable-section">
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details class="expandable-section">
<summary><strong>Properties</strong></summary>


| Property | Example Value |
|----------|---------------|
| `name` | `{{ logbook.name }}` |

</details>

<details>
<summary><strong>Usage Examples</strong></summary>

```django
{% raw %}
&lt;ul&gt;
{% for logbook in digital_logbooks %}
&lt;li&gt;&lt;span class="variable-highlight"&gt;{{ logbook.name }}&lt;/span&gt;&lt;/li&gt;
{% endfor %}
&lt;/ul&gt;
{% endraw %}
```

</details>

---

## login_url

<details class="expandable-section">
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details>
<summary><strong>Usage Examples</strong></summary>

```django
{% raw %}
&lt;tr&gt;
&lt;td align="center" bgcolor="#27a9e3"&gt;
&lt;a style="..." href="&lt;span class="variable-highlight"&gt;{{ login_url }}&lt;/span&gt;"&gt;
Open your contractor portal
&lt;/a&gt;
{% endraw %}
```

</details>

---

## message

<details class="expandable-section">
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details>
<summary><strong>Usage Examples</strong></summary>

```django
{% raw %}
{% endblock %}
&lt;p&gt;A webhook event from Corrigo was rejected.&lt;/p&gt;
&lt;p&gt;Reason: &lt;span class="variable-highlight"&gt;{{ message }}&lt;/span&gt;&lt;/p&gt;
&lt;p&gt;Payload:&lt;p&gt;
&lt;pre&gt;&lt;code&gt;&lt;span class="variable-highlight"&gt;{{payload}}&lt;/span&gt;&lt;/code&gt;&lt;/pre&gt;
{% endraw %}
```

```django
{% raw %}
&lt;span class="variable-highlight"&gt;{{ property_refs|join:", " }}&lt;/span&gt;
&lt;br /&gt;
&lt;span class="variable-highlight"&gt;{{ message }}&lt;/span&gt;
&lt;/li&gt;
&lt;/ul&gt;
{% endraw %}
```

</details>

---

## name

<details class="expandable-section">
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details>
<summary><strong>Usage Examples</strong></summary>

```django
{% raw %}
\{% extends 'email.html' %}
{% block content %}
&lt;p&gt;Your custom report, &lt;span class="variable-highlight"&gt;{{ name }}&lt;/span&gt;, has been generated.&lt;/p&gt;
&lt;p&gt;&lt;span class="variable-highlight"&gt;{{ description }}&lt;/span&gt;&lt;/p&gt;
&lt;p&gt;To download, &lt;a href="&lt;span class="variable-highlight"&gt;{{ csv_url }}&lt;/span&gt;"&gt;please click here&lt;/a&gt;.&lt;/p&gt;
{% endraw %}
```

</details>

---

## no_of_assets

<details class="expandable-section">
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details>
<summary><strong>Usage Examples</strong></summary>

```django
{% raw %}
&lt;p&gt;Regards,&lt;br /&gt;
Uptick Team&lt;/p&gt;
&lt;p&gt;There are currently &lt;span class="variable-highlight"&gt;{{ no_of_assets }}&lt;/span&gt; assets not covered by any Routines. These assets relate to the following properties:&lt;/p&gt;
&lt;ul&gt;
{% for property in properties %}
{% endraw %}
```

</details>

---

## payload

<details class="expandable-section">
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details>
<summary><strong>Usage Examples</strong></summary>

```django
{% raw %}
&lt;p&gt;Reason: &lt;span class="variable-highlight"&gt;{{ message }}&lt;/span&gt;&lt;/p&gt;
&lt;p&gt;Payload:&lt;p&gt;
&lt;pre&gt;&lt;code&gt;&lt;span class="variable-highlight"&gt;{{payload}}&lt;/span&gt;&lt;/code&gt;&lt;/pre&gt;
&lt;p&gt;Regards,&lt;br /&gt;
Uptick Team&lt;/p&gt;
{% endraw %}
```

</details>

---

## promptset

<details class="expandable-section">
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details class="expandable-section">
<summary><strong>Properties</strong></summary>


| Property | Example Value |
|----------|---------------|
| `name` | `{{ promptset.name }}` |
| `ref` | `{{ promptset.ref }}` |

</details>

<details>
<summary><strong>Usage Examples</strong></summary>

```django
{% raw %}
&lt;tr&gt;
&lt;th colspan="3" class="border-top-0"&gt;
(&lt;span class="variable-highlight"&gt;{{ promptset.ref }}&lt;/span&gt;) &lt;span class="variable-highlight"&gt;{{ promptset.name }}&lt;/span&gt;
&lt;/th&gt;
&lt;/tr&gt;
{% endraw %}
```

</details>

---

## property
<div class="loop-info">Loop Iterator<span class="tooltip">This variable represents a single item from a list or collection being looped over.</span></div>

<details class="expandable-section">
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details class="expandable-section">
<summary><strong>Properties</strong></summary>


| Property | Example Value |
|----------|---------------|
| `client_ref` | `{{ property.client_ref }}` |
| `name` | `{{ property.name }}` |
| `property__name` | `{{ property.property__name }}` |
| `property_id` | `{{property.property_id}}` |
| `ref` | `{{ property.ref }}` |

</details>

<details>
<summary><strong>Usage Examples</strong></summary>

```django
{% raw %}
{% endblock %}
&lt;p&gt;Dear &lt;span class="variable-highlight"&gt;{{ attention }}&lt;/span&gt;,&lt;/p&gt;
&lt;p&gt;Please find attached your defect quote for &lt;span class="variable-highlight"&gt;{{ property.name }}&lt;/span&gt;.&lt;/p&gt;
&lt;p&gt;To view and approve this quote online, visit:&lt;/p&gt;
&lt;p&gt;&lt;a href="&lt;span class="variable-highlight"&gt;{{ base_url }}&lt;/span&gt;&lt;span class="variable-highlight"&gt;{{ quote.get_uuid_approval_url }}&lt;/span&gt;"&gt;&lt;span class="variable-highlight"&gt;{{ base_url }}&lt;/span&gt;&lt;span class="variable-highlight"&gt;{{ quote.get_uuid_approval_url }}&lt;/span&gt;&lt;/a&gt;&lt;/p&gt;
{% endraw %}
```

```django
{% raw %}
&lt;span class="variable-highlight"&gt;{{ config.SITE_ORGANISATION }}&lt;/span&gt;&lt;/p&gt;
&lt;p&gt;Dear &lt;span class="variable-highlight"&gt;{{ attention|default:"manager" }}&lt;/span&gt;,&lt;/p&gt;
&lt;p&gt;Please find attached your documents for services recently carried out at &lt;span class="variable-highlight"&gt;{{ property.name }}&lt;/span&gt;.&lt;/p&gt;
{% if invoice %}
&lt;p&gt;Your invoice:&lt;/p&gt;
{% endraw %}
```

```django
{% raw %}
&lt;p&gt;For any questions, please contact us.&lt;/p&gt;
&lt;p&gt;Dear &lt;span class="variable-highlight"&gt;{{ attention|default:"manager" }}&lt;/span&gt;,&lt;/p&gt;
&lt;p&gt;Please find attached your documents for services recently carried out at &lt;span class="variable-highlight"&gt;{{ property.name }}&lt;/span&gt;.&lt;/p&gt;
{% if invoice %}
&lt;p&gt;Your invoice:&lt;/p&gt;
{% endraw %}
```

</details>

---

## purchaseorder

<details class="expandable-section">
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details class="expandable-section">
<summary><strong>Properties</strong></summary>


| Property | Example Value |
|----------|---------------|
| `delivery_instructions` | `{{purchaseorder.delivery_instructions}}` |

</details>

<details>
<summary><strong>Usage Examples</strong></summary>

```django
{% raw %}
&lt;p&gt;Dear &lt;span class="variable-highlight"&gt;{{ attention }}&lt;/span&gt;,&lt;/p&gt;
&lt;p&gt;Please find attached our purchase order{% if task %} for &lt;span class="variable-highlight"&gt;{{ task.name }}&lt;/span&gt;{% endif %}.&lt;/p&gt;
&lt;p&gt;Please deliver the parts to &lt;span class="variable-highlight"&gt;{{purchaseorder.delivery_instructions}}&lt;/span&gt; &lt;/p&gt;
&lt;p&gt;&lt;strong&gt;Delivery Address:&lt;strong&gt;&lt;/p&gt;
&lt;p&gt;Regards,&lt;br /&gt;
{% endraw %}
```

</details>

---

## quote
<div class="loop-info">Loop Iterator<span class="tooltip">This variable represents a single item from a list or collection being looped over.</span></div>

<details class="expandable-section">
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details class="expandable-section">
<summary><strong>Properties</strong></summary>


| Property | Example Value |
|----------|---------------|
| `get_uuid_approval_url` | `{{ quote.get_uuid_approval_url\|absolute }}` |
| `property.name` | `{{ quote.property.name }}` |
| `ref` | `{{ quote.ref }}` |
| `status.upper` | `{{ quote.status.upper }}` |

</details>

<details class="expandable-section">
<summary><strong>Filters Used</strong></summary>

- `absolute`

</details>

<details>
<summary><strong>Usage Examples</strong></summary>

```django
{% raw %}
&lt;p&gt;Please find attached your defect quote for &lt;span class="variable-highlight"&gt;{{ property.name }}&lt;/span&gt;.&lt;/p&gt;
&lt;p&gt;To view and approve this quote online, visit:&lt;/p&gt;
&lt;p&gt;&lt;a href="&lt;span class="variable-highlight"&gt;{{ base_url }}&lt;/span&gt;&lt;span class="variable-highlight"&gt;{{ quote.get_uuid_approval_url }}&lt;/span&gt;"&gt;&lt;span class="variable-highlight"&gt;{{ base_url }}&lt;/span&gt;&lt;span class="variable-highlight"&gt;{{ quote.get_uuid_approval_url }}&lt;/span&gt;&lt;/a&gt;&lt;/p&gt;
&lt;p&gt;We value your opinion, please contact us with any comments you may have.&lt;/p&gt;
&lt;p&gt;Regards,&lt;br /&gt;
{% endraw %}
```

```django
{% raw %}
&lt;ul&gt;
{% for quote in defectquotes %}
&lt;li&gt;Reference: &lt;span class="variable-highlight"&gt;{{ quote.ref }}&lt;/span&gt;&lt;a href="&lt;span class="variable-highlight"&gt;{{ base_url }}&lt;/span&gt;&lt;span class="variable-highlight"&gt;{{ quote.get_uuid_approval_url }}&lt;/span&gt;"&gt; (approve online)&lt;/a&gt;&lt;/li&gt;
{% endfor %}
&lt;/ul&gt;
{% endraw %}
```

```django
{% raw %}
{% endif %}
&lt;p&gt;To view and approve this quote online, visit:&lt;/p&gt;
&lt;p&gt;&lt;a href="&lt;span class="variable-highlight"&gt;{{ base_url }}&lt;/span&gt;&lt;span class="variable-highlight"&gt;{{ quote.get_uuid_approval_url }}&lt;/span&gt;"&gt;&lt;span class="variable-highlight"&gt;{{ base_url }}&lt;/span&gt;&lt;span class="variable-highlight"&gt;{{ quote.get_uuid_approval_url }}&lt;/span&gt;&lt;/a&gt;&lt;/p&gt;
&lt;p&gt;Regards,&lt;br /&gt;
&lt;span class="variable-highlight"&gt;{{ config.SITE_ORGANISATION }}&lt;/span&gt;&lt;/p&gt;
{% endraw %}
```

</details>

---

## rectification

<details class="expandable-section">
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details class="expandable-section">
<summary><strong>Properties</strong></summary>


| Property | Example Value |
|----------|---------------|
| `ref` | `{{ rectification.ref }}` |
| `rejection_reason` | `{{ rectification.rejection_reason\|markdowner }}` |

</details>

<details class="expandable-section">
<summary><strong>Filters Used</strong></summary>

- `markdowner`

</details>

<details>
<summary><strong>Usage Examples</strong></summary>

```django
{% raw %}
{% load markdowner %}
{% block content %}
&lt;h4&gt;Rectification &lt;span class="variable-highlight"&gt;{{ rectification.ref }}&lt;/span&gt; was rejected.&lt;/h4&gt;
&lt;p&gt;Reason provided:&lt;/p&gt;
&lt;span class="variable-highlight"&gt;{{ rectification.rejection_reason|markdowner }}&lt;/span&gt;
{% endraw %}
```

```django
{% raw %}
&lt;h4&gt;Rectification &lt;span class="variable-highlight"&gt;{{ rectification.ref }}&lt;/span&gt; was rejected.&lt;/h4&gt;
&lt;p&gt;Reason provided:&lt;/p&gt;
&lt;span class="variable-highlight"&gt;{{ rectification.rejection_reason|markdowner }}&lt;/span&gt;
&lt;p&gt;Access the rectification to provide updated information:&lt;/p&gt;
&lt;p&gt;&lt;a href="&lt;span class="variable-highlight"&gt;{{ base_url }}&lt;/span&gt;&lt;span class="variable-highlight"&gt;{{ absolute_url }}&lt;/span&gt;"&gt;&lt;span class="variable-highlight"&gt;{{ base_url }}&lt;/span&gt;&lt;span class="variable-highlight"&gt;{{ absolute_url }}&lt;/span&gt;&lt;/a&gt;&lt;/p&gt;
{% endraw %}
```

</details>

---

## ref_no

<details class="expandable-section">
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details>
<summary><strong>Usage Examples</strong></summary>

```django
{% raw %}
&lt;tr&gt;
&lt;td style="..."&gt;OUR REF NO.&lt;/td&gt;
&lt;td style="..." colspan="3"&gt;&lt;span class="variable-highlight"&gt;{{ref_no}}&lt;/span&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
{% endraw %}
```

```django
{% raw %}
&lt;tr&gt;
&lt;td style="..."&gt;VISIT No.&lt;/td&gt;
&lt;td style="..." colspan="3"&gt;&lt;span class="variable-highlight"&gt;{{ref_no}}&lt;/span&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
{% endraw %}
```

</details>

---

## rejection_reason

<details class="expandable-section">
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details>
<summary><strong>Usage Examples</strong></summary>

```django
{% raw %}
&lt;p&gt;You can provide your field technicians with this link which will enable them to complete the task via their smart phone (apple or android) without needing to install an app.&lt;/p&gt;
&lt;p&gt;Thanks&lt;/p&gt;
&lt;p&gt;The contractor &lt;span class="variable-highlight"&gt;{{ contractor }}&lt;/span&gt; has rejected the task assigned to him for the following reason: &lt;span class="variable-highlight"&gt;{{ rejection_reason }}&lt;/span&gt;&lt;/p&gt;
&lt;p&gt;
The task that was assigned was:&lt;br&gt;
{% endraw %}
```

</details>

---

## remark
<div class="loop-info">Loop Iterator<span class="tooltip">This variable represents a single item from a list or collection being looped over.</span></div>

<details class="expandable-section">
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details class="expandable-section">
<summary><strong>Properties</strong></summary>


| Property | Example Value |
|----------|---------------|
| `get_description` | `{{ remark.get_description\|markdowner }}` |
| `get_public_url` | `{{ remark.get_public_url }}` |
| `get_resolution` | `{{ remark.get_resolution\|markdowner }}` |
| `get_severity_display` | `{{ remark.get_severity_display }}` |
| `id` | `{{ remark.id }}` |
| `identified` | `{{ remark.identified }}` |
| `last_verified_date` | `{{ remark.last_verified_date }}` |
| `location` | `{{ remark.location\|markdowner }}` |
| `severity` | `{{ remark.severity }}` |

</details>

<details class="expandable-section">
<summary><strong>Filters Used</strong></summary>

- `markdowner`

</details>

<details>
<summary><strong>Usage Examples</strong></summary>

```django
{% raw %}
&lt;tr&gt;
&lt;td class="m-0 p-0"&gt;
&lt;div id="&lt;span class="variable-highlight"&gt;{{ remark.id }}&lt;/span&gt;"
class="remark severity-&lt;span class="variable-highlight"&gt;{{ remark.severity }}&lt;/span&gt; keep-together"&gt;
&lt;div class="d-flex flex-row justify-content-between header"&gt;
{% endraw %}
```

```django
{% raw %}
&lt;td class="m-0 p-0"&gt;
&lt;div id="&lt;span class="variable-highlight"&gt;{{ remark.id }}&lt;/span&gt;"
class="remark severity-&lt;span class="variable-highlight"&gt;{{ remark.severity }}&lt;/span&gt; keep-together"&gt;
&lt;div class="d-flex flex-row justify-content-between header"&gt;
&lt;div class="px-3 py-2"&gt;
{% endraw %}
```

```django
{% raw %}
&lt;div class="d-flex flex-row justify-content-between header"&gt;
&lt;div class="px-3 py-2"&gt;
&lt;strong&gt;&lt;span class="variable-highlight"&gt;{{ remark.get_severity_display }}&lt;/span&gt;&lt;/strong&gt;
&lt;br/&gt;
&lt;a href="&lt;span class="variable-highlight"&gt;{{ remark.get_public_url }}&lt;/span&gt;"&gt;
{% endraw %}
```

</details>

---

## report
<div class="loop-info">Loop Iterator<span class="tooltip">This variable represents a single item from a list or collection being looped over.</span></div>

<details class="expandable-section">
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details class="expandable-section">
<summary><strong>Properties</strong></summary>


| Property | Example Value |
|----------|---------------|
| `get_title` | `{{ report.get_title }}` |

</details>

<details>
<summary><strong>Usage Examples</strong></summary>

```django
{% raw %}
&lt;ul&gt;
{% for report in reports %}
&lt;li&gt;&lt;span class="variable-highlight"&gt;{{ report.get_title }}&lt;/span&gt; (&lt;span class="variable-highlight"&gt;{{ report.compliant|yesno:"compliant,non-compliant,not applicable"}}&lt;/span&gt;)&lt;/li&gt;
{% endfor %}
&lt;/ul&gt;
{% endraw %}
```

</details>

---

## request_user

<details class="expandable-section">
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details class="expandable-section">
<summary><strong>Properties</strong></summary>


| Property | Example Value |
|----------|---------------|
| `email` | `{{request_user.email}}` |
| `name` | `{{request_user.name}}` |

</details>

<details>
<summary><strong>Usage Examples</strong></summary>

```django
{% raw %}
&lt;/tbody&gt;
&lt;/table&gt;
&lt;p&gt;If you have any queries or need to change the time, please email me at &lt;a href="mailto:&lt;span class="variable-highlight"&gt;{{request_user.email}}&lt;/span&gt;"&gt;&lt;span class="variable-highlight"&gt;{{request_user.email}}&lt;/span&gt;&lt;/a&gt;.&lt;/p&gt;
&lt;p&gt;Regards,&lt;br&gt;
&lt;span class="variable-highlight"&gt;{{request_user.name}}&lt;/span&gt;&lt;/p&gt;
{% endraw %}
```

```django
{% raw %}
&lt;p&gt;If you have any queries or need to change the time, please email me at &lt;a href="mailto:&lt;span class="variable-highlight"&gt;{{request_user.email}}&lt;/span&gt;"&gt;&lt;span class="variable-highlight"&gt;{{request_user.email}}&lt;/span&gt;&lt;/a&gt;.&lt;/p&gt;
&lt;p&gt;Regards,&lt;br&gt;
&lt;span class="variable-highlight"&gt;{{request_user.name}}&lt;/span&gt;&lt;/p&gt;
&lt;p&gt;&lt;span class="variable-highlight"&gt;{{request_user.email}}&lt;/span&gt;&lt;/p&gt;
&lt;p&gt;
{% endraw %}
```

```django
{% raw %}
&lt;p&gt;Regards,&lt;br&gt;
&lt;span class="variable-highlight"&gt;{{request_user.name}}&lt;/span&gt;&lt;/p&gt;
&lt;p&gt;&lt;span class="variable-highlight"&gt;{{request_user.email}}&lt;/span&gt;&lt;/p&gt;
&lt;p&gt;
&lt;span class="variable-highlight"&gt;{{ config.CONTACT_PHONE }}&lt;/span&gt; &lt;br /&gt;
{% endraw %}
```

</details>

---

## retry_link

<details class="expandable-section">
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details>
<summary><strong>Usage Examples</strong></summary>

```django
{% raw %}
&lt;p&gt;Please review and address the error, then use the link below to retry the sync&lt;/p&gt;
&lt;p&gt;
&lt;a href=&lt;span class="variable-highlight"&gt;{{ retry_link }}&lt;/span&gt;&gt;Click here&lt;/a&gt; and use the &lt;code&gt;POST&lt;/code&gt; button to retry the sync.
&lt;/p&gt;
&lt;h3&gt;Error&lt;/h3&gt;
{% endraw %}
```

</details>

---

## routineserviceleveltype

<details class="expandable-section">
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details class="expandable-section">
<summary><strong>Properties</strong></summary>


| Property | Example Value |
|----------|---------------|
| `get_routine_display_name` | `{{ routineserviceleveltype.get_routine_display_name }}` |
| `routineservicetype.standard.name` | `{{ routineserviceleveltype.routineservicetype.standard.name }}` |

</details>

<details>
<summary><strong>Usage Examples</strong></summary>

```django
{% raw %}
{% for routineserviceleveltype, servicetask_group in servicetasks_grouped_by_type %}
&lt;div class="uptick-title no-page-break-after"&gt;
&lt;div&gt;&lt;span class="variable-highlight"&gt;{{ routineserviceleveltype.get_routine_display_name }}&lt;/span&gt;&lt;/div&gt;
{% if routineserviceleveltype.routineservicetype.standard.name != "Default" %}
&lt;div className="text-muted"&gt;&lt;small&gt;&lt;span class="variable-highlight"&gt;{{ routineserviceleveltype.routineservicetype.standard.name }}&lt;/span&gt;&lt;/small&gt;&lt;/div&gt;
{% endraw %}
```

```django
{% raw %}
&lt;div&gt;&lt;span class="variable-highlight"&gt;{{ routineserviceleveltype.get_routine_display_name }}&lt;/span&gt;&lt;/div&gt;
{% if routineserviceleveltype.routineservicetype.standard.name != "Default" %}
&lt;div className="text-muted"&gt;&lt;small&gt;&lt;span class="variable-highlight"&gt;{{ routineserviceleveltype.routineservicetype.standard.name }}&lt;/span&gt;&lt;/small&gt;&lt;/div&gt;
{% endif %}
&lt;/div&gt;
{% endraw %}
```

</details>

---

## rslt
<div class="loop-info">Loop Iterator<span class="tooltip">This variable represents a single item from a list or collection being looped over.</span></div>

<details class="expandable-section">
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details class="expandable-section">
<summary><strong>Properties</strong></summary>


| Property | Example Value |
|----------|---------------|
| `name` | `{{ rslt.name }}` |

</details>

<details>
<summary><strong>Usage Examples</strong></summary>

```django
{% raw %}
&lt;span class="variable-highlight"&gt;{{ line.routineservicetype.name }}&lt;/span&gt; –
{% for rslt in line.routineserviceleveltypes.all %}
&lt;span&gt;&lt;span class="variable-highlight"&gt;{{ rslt.name }}&lt;/span&gt;{% if not forloop.last %}, {% endif %}&lt;/span&gt;
{% endfor %}
&lt;/div&gt;
{% endraw %}
```

```django
{% raw %}
&lt;div&gt;&lt;span class="variable-highlight"&gt;{{ line.routineservicetype.name }}&lt;/span&gt;&lt;/div&gt;
{% for rslt in line.routineserviceleveltypes.all %}
&lt;span&gt;&lt;span class="variable-highlight"&gt;{{ rslt.name }}&lt;/span&gt;{% if not forloop.last %},{% endif %}&lt;/span&gt;
{% endfor %}
&lt;/div&gt;
{% endraw %}
```

</details>

---

## scope_of_works

<details class="expandable-section">
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details>
<summary><strong>Usage Examples</strong></summary>

```django
{% raw %}
&lt;tr&gt;
&lt;td style="..."&gt;SCOPE OF WORKS&lt;/td&gt;
&lt;td style="..." colspan="3"&gt;&lt;span class="variable-highlight"&gt;{{scope_of_works}}&lt;/span&gt;&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
{% endraw %}
```

</details>

---

## sender

<details class="expandable-section">
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details class="expandable-section">
<summary><strong>Properties</strong></summary>


| Property | Example Value |
|----------|---------------|
| `name` | `{{ sender.name }}` |

</details>

<details>
<summary><strong>Usage Examples</strong></summary>

```django
{% raw %}
&lt;p&gt;Template change request &lt;span class="variable-highlight"&gt;{{ changerequest.ref }}&lt;/span&gt; has been created for &lt;span class="variable-highlight"&gt;{{ customer }}&lt;/span&gt;.&lt;/p&gt;
{% elif  status == 'REQUESTED' %}
&lt;p&gt;&lt;span class="variable-highlight"&gt;{{ sender.name }}&lt;/span&gt; submitted feedback for Template change request &lt;span class="variable-highlight"&gt;{{ changerequest.ref }}&lt;/span&gt;.&lt;/p&gt;
{% else %}
&lt;p&gt;Template change request &lt;span class="variable-highlight"&gt;{{ changerequest.ref }}&lt;/span&gt; has been approved. Our team will be in contact once completed.&lt;/p&gt;
{% endraw %}
```

</details>

---

## servicequote

<details class="expandable-section">
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details class="expandable-section">
<summary><strong>Properties</strong></summary>


| Property | Example Value |
|----------|---------------|
| `annual_gst` | `{{ servicequote.annual_gst\|currency }}` |
| `annual_subtotal` | `{{ servicequote.annual_subtotal\|currency }}` |
| `annual_total` | `{{ servicequote.annual_total\|currency }}` |
| `description` | `{{ servicequote.description }}` |
| `expiry_date` | `{{ servicequote.expiry_date }}` |
| `get_absolute_url` | `{{ servicequote.get_absolute_url }}` |
| `product_gst` | `{{ servicequote.product_gst\|currency }}` |
| `product_subtotal` | `{{ servicequote.product_subtotal\|currency }}` |
| `product_total` | `{{ servicequote.product_total\|currency }}` |
| `ref` | `{{ servicequote.ref }}` |
| `salesperson.email` | `{{ servicequote.salesperson.email }}` |
| `salesperson.name` | `{{ servicequote.salesperson.name }}` |
| `scope_of_works` | `{{ servicequote.scope_of_works\|markdowner }}` |
| `terms_and_conditions` | `{{ servicequote.terms_and_conditions\|markdowner }}` |

</details>

<details class="expandable-section">
<summary><strong>Filters Used</strong></summary>

- `currency`
- `markdowner`

</details>

<details>
<summary><strong>Usage Examples</strong></summary>

```django
{% raw %}
&lt;div&gt;
&lt;strong&gt;Scope of works:&lt;/strong&gt;
&lt;span class="variable-highlight"&gt;{{ servicequote.description }}&lt;/span&gt;
&lt;/div&gt;
&lt;br /&gt;
{% endraw %}
```

```django
{% raw %}
Kind regards,&lt;br /&gt;&lt;br /&gt;
{% if servicequote.salesperson %}
&lt;div&gt;&lt;span class="variable-highlight"&gt;{{ servicequote.salesperson.name }}&lt;/span&gt;&lt;/div&gt;
&lt;div&gt;&lt;span class="variable-highlight"&gt;{{ servicequote.salesperson.email }}&lt;/span&gt;&lt;/div&gt;
{% endif %}
{% endraw %}
```

```django
{% raw %}
{% if servicequote.salesperson %}
&lt;div&gt;&lt;span class="variable-highlight"&gt;{{ servicequote.salesperson.name }}&lt;/span&gt;&lt;/div&gt;
&lt;div&gt;&lt;span class="variable-highlight"&gt;{{ servicequote.salesperson.email }}&lt;/span&gt;&lt;/div&gt;
{% endif %}
&lt;p&gt;&lt;span class="variable-highlight"&gt;{{ config.SITE_ORGANISATION }}&lt;/span&gt;&lt;/p&gt;
{% endraw %}
```

</details>

---

## servicetask
<div class="loop-info">Loop Iterator<span class="tooltip">This variable represents a single item from a list or collection being looped over.</span></div>

<details class="expandable-section">
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details class="expandable-section">
<summary><strong>Properties</strong></summary>


| Property | Example Value |
|----------|---------------|
| `get_result_display.upper` | `{{ servicetask.get_result_display.upper }}` |
| `item` | `{{ servicetask.item\|bsecure_url }}` |
| `item.extra_fields.door_depth` | `{{servicetask.item.extra_fields.door_depth}}` |
| `item.extra_fields.door_width` | `{{servicetask.item.extra_fields.door_width}}` |
| `item.get_extra_fields_display.certification_id_present` | `{{servicetask.item.get_extra_fields_display.certification_id_present}}` |
| `item.get_extra_fields_display.comments` | `{{servicetask.item.get_extra_fields_display.comments}}` |
| `item.get_extra_fields_display.door_height` | `{{servicetask.item.get_extra_fields_display.door_height}}` |
| `item.get_extra_fields_display.door_material` | `{{servicetask.item.get_extra_fields_display.door_material}}` |
| `item.get_extra_fields_display.door_rating` | `{{servicetask.item.get_extra_fields_display.door_rating}}` |
| `item.get_extra_fields_display.frame_material` | `{{servicetask.item.get_extra_fields_display.frame_material}}` |
| `item.get_label` | `{{ servicetask.item.get_label }}` |
| `item.inspection_ref` | `{{ servicetask.item.inspection_ref }}` |
| `item.location` | `{{ servicetask.item.location }}` |
| `result` | `{{ servicetask.result }}` |

</details>

<details class="expandable-section">
<summary><strong>Filters Used</strong></summary>

- `bsecure_badge_code`
- `bsecure_url`

</details>

<details>
<summary><strong>Usage Examples</strong></summary>

```django
{% raw %}
&lt;tbody&gt;
&lt;tr class="keep-together bottom-border"&gt;
&lt;th width="35%" class="bg-white"&gt;&lt;span class="variable-highlight"&gt;{{ servicetask.item.get_label }}&lt;/span&gt;&lt;/th&gt;
&lt;th width="50%" class="bg-white light-text-weight"&gt;
{% if servicetask.item.inspection_ref %}
{% endraw %}
```

```django
{% raw %}
&lt;th width="50%" class="bg-white light-text-weight"&gt;
{% if servicetask.item.inspection_ref %}
&lt;strong&gt;Serial:&lt;/strong&gt; &lt;span class="variable-highlight"&gt;{{ servicetask.item.inspection_ref }}&lt;/span&gt;
{% endif %}
{% if servicetask.item.bsecure_latest_sticker_guid %}
{% endraw %}
```

```django
{% raw %}
{% endif %}
{% if servicetask.item.bsecure_latest_sticker_guid %}
&lt;a href="&lt;span class="variable-highlight"&gt;{{ servicetask.item|bsecure_url }}&lt;/span&gt;"&gt;
&lt;strong&gt;BSecure:&lt;/strong&gt; &lt;span class="variable-highlight"&gt;{{ servicetask.item|bsecure_badge_code }}&lt;/span&gt;
{% include "reports/library/arrow-up-right-from-square-icon.svg" with width="11" height="11" %}
{% endraw %}
```

</details>

---

## signoff

<details class="expandable-section">
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details class="expandable-section">
<summary><strong>Properties</strong></summary>


| Property | Example Value |
|----------|---------------|
| `account` | `{{ signoff.account }}` |
| `contractor` | `{{ signoff.contractor }}` |
| `period_finish` | `{{ signoff.period_finish }}` |
| `period_start` | `{{ signoff.period_start}}` |
| `pk` | `{{ signoff.pk }}` |

</details>

<details>
<summary><strong>Usage Examples</strong></summary>

```django
{% raw %}
{% extends 'email.html' %}
{% block content %}
&lt;h3&gt;Contractor sign off &lt;span class="variable-highlight"&gt;{{ signoff.pk }}&lt;/span&gt; results for &lt;span class="variable-highlight"&gt;{{ signoff.contractor }}&lt;/span&gt;&lt;/h3&gt;
&lt;h4&gt;Submitted by &lt;span class="variable-highlight"&gt;{{ signoff.account }}&lt;/span&gt; for &lt;span class="variable-highlight"&gt;{{ signoff.period_start}}&lt;/span&gt; to &lt;span class="variable-highlight"&gt;{{ signoff.period_finish }}&lt;/span&gt;.&lt;/h4&gt;
{% for signoffproperty in signoff.signoffproperty_set.all %}
{% endraw %}
```

```django
{% raw %}
{% block content %}
&lt;h3&gt;Contractor sign off &lt;span class="variable-highlight"&gt;{{ signoff.pk }}&lt;/span&gt; results for &lt;span class="variable-highlight"&gt;{{ signoff.contractor }}&lt;/span&gt;&lt;/h3&gt;
&lt;h4&gt;Submitted by &lt;span class="variable-highlight"&gt;{{ signoff.account }}&lt;/span&gt; for &lt;span class="variable-highlight"&gt;{{ signoff.period_start}}&lt;/span&gt; to &lt;span class="variable-highlight"&gt;{{ signoff.period_finish }}&lt;/span&gt;.&lt;/h4&gt;
{% for signoffproperty in signoff.signoffproperty_set.all %}
&lt;h5&gt;&lt;span class="variable-highlight"&gt;{{ signoffproperty.property }}&lt;/span&gt;&lt;/h5&gt;
{% endraw %}
```

</details>

---

## signoffitem
<div class="loop-info">Loop Iterator<span class="tooltip">This variable represents a single item from a list or collection being looped over.</span></div>

<details class="expandable-section">
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details class="expandable-section">
<summary><strong>Properties</strong></summary>


| Property | Example Value |
|----------|---------------|
| `label` | `{{ signoffitem.label }}` |
| `new_serviced_date` | `{{ signoffitem.new_serviced_date }}` |
| `new_signoff_note` | `{{ signoffitem.new_signoff_note }}` |

</details>

<details>
<summary><strong>Usage Examples</strong></summary>

```django
{% raw %}
{% endif %}
]
&lt;span class="variable-highlight"&gt;{{ signoffitem.label }}&lt;/span&gt;
{% if signoffitem.new_signoff_note %}
&lt;div style="..."&gt;Note: &lt;span class="variable-highlight"&gt;{{ signoffitem.new_signoff_note }}&lt;/span&gt;&lt;/div&gt;
{% endraw %}
```

```django
{% raw %}
&lt;span class="variable-highlight"&gt;{{ signoffitem.label }}&lt;/span&gt;
{% if signoffitem.new_signoff_note %}
&lt;div style="..."&gt;Note: &lt;span class="variable-highlight"&gt;{{ signoffitem.new_signoff_note }}&lt;/span&gt;&lt;/div&gt;
{% endif %}
{% if signoffitem.new_serviced_date %}
{% endraw %}
```

```django
{% raw %}
{% endif %}
{% if signoffitem.new_serviced_date %}
&lt;div style="..."&gt;Service date: &lt;span class="variable-highlight"&gt;{{ signoffitem.new_serviced_date }}&lt;/span&gt;&lt;/div&gt;
{% endif %}
&lt;/li&gt;
{% endraw %}
```

</details>

---

## signoffproperties

<details class="expandable-section">
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details class="expandable-section">
<summary><strong>Filters Used</strong></summary>

- `pluralize`

</details>

<details>
<summary><strong>Usage Examples</strong></summary>

```django
{% raw %}
{% extends 'email.html' %}
{% block content %}
&lt;h4&gt;Request&lt;span class="variable-highlight"&gt;{{ signoffproperties|pluralize }}&lt;/span&gt; for &lt;span class="variable-highlight"&gt;{{ contractor.name }}&lt;/span&gt; (&lt;span class="variable-highlight"&gt;{{ contractor.account }}&lt;/span&gt;).&lt;/h4&gt;
&lt;p&gt;In order to issue compliant reports, we require confirmation that you, as a service contractor, have serviced the relevant Essential Safety Measures to Australian Standards over the previous 12 months.&lt;/p&gt;
&lt;table border="0" cellpadding="10" cellspacing="0" bgcolor="#27a9e3" width="100%"&gt;
{% endraw %}
```

```django
{% raw %}
{% endfor %}
&lt;/ul&gt;
&lt;p&gt;If the form&lt;span class="variable-highlight"&gt;{{ signoffproperties|pluralize }}&lt;/span&gt; on the attached link &lt;span class="variable-highlight"&gt;{{ signoffproperties|pluralize:"is,are" }}&lt;/span&gt; not submitted within the next 30 days and there is no proof on site that the Essential Safety Measures are being serviced, &lt;span class="variable-highlight"&gt;{{ signoffproperties|pluralize:"a," }}&lt;/span&gt; Non-Compliant Building Report&lt;span class="variable-highlight"&gt;{{ signoffproperties|pluralize }}&lt;/span&gt; will be issued.&lt;/p&gt;
{% endblock %}
{% extends 'email.html' %}
{% endraw %}
```

```django
{% raw %}
{% endfor %}
&lt;/ul&gt;
&lt;p&gt;If the form&lt;span class="variable-highlight"&gt;{{ signoffproperties|pluralize }}&lt;/span&gt; on the attached link &lt;span class="variable-highlight"&gt;{{ signoffproperties|pluralize:"is,are" }}&lt;/span&gt; not submitted and there is no proof on site that the Essential Safety Measures are being serviced, &lt;span class="variable-highlight"&gt;{{ signoffproperties|pluralize:"a," }}&lt;/span&gt; Non-Compliant Building Report&lt;span class="variable-highlight"&gt;{{ signoffproperties|pluralize }}&lt;/span&gt; will be issued.&lt;/p&gt;
{% endblock %}
&lt;p&gt;Dear &lt;span class="variable-highlight"&gt;{{ client.primary_contact.name }}&lt;/span&gt;,&lt;/p&gt;
{% endraw %}
```

</details>

---

## signoffproperty
<div class="loop-info">Loop Iterator<span class="tooltip">This variable represents a single item from a list or collection being looped over.</span></div>

<details class="expandable-section">
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details class="expandable-section">
<summary><strong>Properties</strong></summary>


| Property | Example Value |
|----------|---------------|
| `created` | `{{ signoffproperty.created\|date }}` |
| `disclaimed_reason` | `{{signoffproperty.disclaimed_reason}}` |
| `due` | `{{ signoffproperty.due\|date }}` |
| `is_disclaimed` | `{{ signoffproperty.is_disclaimed }}` |
| `note` | `{{ signoffproperty.note }}` |
| `property` | `{{ signoffproperty.property }}` |
| `property.name` | `{{ signoffproperty.property.name }}` |

</details>

<details class="expandable-section">
<summary><strong>Filters Used</strong></summary>

- `date`

</details>

<details>
<summary><strong>Usage Examples</strong></summary>

```django
{% raw %}
{% for signoffproperty in signoffproperties %}
&lt;li&gt;
&lt;h5&gt;&lt;span class="variable-highlight"&gt;{{ signoffproperty.property.name }}&lt;/span&gt;&lt;/h5&gt;
&lt;p&gt;
Due: &lt;span class="variable-highlight"&gt;{{ signoffproperty.due|date }}&lt;/span&gt;
{% endraw %}
```

```django
{% raw %}
&lt;h5&gt;&lt;span class="variable-highlight"&gt;{{ signoffproperty.property.name }}&lt;/span&gt;&lt;/h5&gt;
&lt;p&gt;
Due: &lt;span class="variable-highlight"&gt;{{ signoffproperty.due|date }}&lt;/span&gt;
&lt;/p&gt;
&lt;/li&gt;
{% endraw %}
```

```django
{% raw %}
{% for signoffproperty in signoffproperties %}
&lt;li&gt;
&lt;h5&gt;&lt;span class="variable-highlight"&gt;{{ signoffproperty.property.name }}&lt;/span&gt;&lt;/h5&gt;
&lt;p&gt;
Due: &lt;span class="variable-highlight"&gt;{{ signoffproperty.due|date }}&lt;/span&gt;&lt;br/&gt;
{% endraw %}
```

</details>

---

## start_date

<details class="expandable-section">
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details>
<summary><strong>Usage Examples</strong></summary>

```django
{% raw %}
&lt;tr&gt;
&lt;td style="..."&gt;START DATE&lt;/td&gt;
&lt;td style="..."&gt;&lt;span class="variable-highlight"&gt;{{start_date}}&lt;/span&gt;&lt;/td&gt;
&lt;td style="..."&gt;END DATE&lt;/td&gt;
&lt;td style="..."&gt;&lt;span class="variable-highlight"&gt;{{end_date}}&lt;/span&gt;&lt;/td&gt;
{% endraw %}
```

</details>

---

## subject

<details class="expandable-section">
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details>
<summary><strong>Usage Examples</strong></summary>

```django
{% raw %}
To: &lt;span class="variable-highlight"&gt;{{ to_list }}&lt;/span&gt;&lt;br /&gt;
CC: &lt;span class="variable-highlight"&gt;{{ cc_list }}&lt;/span&gt;&lt;br /&gt;
Subject &lt;span class="variable-highlight"&gt;{{ subject }}&lt;/span&gt;&lt;br /&gt;
&lt;/p&gt;
&lt;p&gt;
{% endraw %}
```

```django
{% raw %}
Address: &lt;span class="variable-highlight"&gt;{{ bounce_address }}&lt;/span&gt;&lt;br /&gt;
Bounce Reason: &lt;span class="variable-highlight"&gt;{{ formatted_reason }}&lt;/span&gt;&lt;br /&gt;
Email Subject &lt;span class="variable-highlight"&gt;{{ subject }}&lt;/span&gt;&lt;br /&gt;
Email Sent: &lt;span class="variable-highlight"&gt;{{ formatted_timestamp }}&lt;/span&gt;
&lt;/p&gt;
{% endraw %}
```

</details>

---

## task
<div class="loop-info">Loop Iterator<span class="tooltip">This variable represents a single item from a list or collection being looped over.</span></div>

<details class="expandable-section">
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details class="expandable-section">
<summary><strong>Properties</strong></summary>


| Property | Example Value |
|----------|---------------|
| `address` | `{{ task.address }}` |
| `description` | `{{ task.description }}` |
| `name` | `{{ task.name }}` |
| `property.name` | `{{ task.property.name }}` |
| `ref` | `{{ task.ref }}` |

</details>

<details>
<summary><strong>Usage Examples</strong></summary>

```django
{% raw %}
{% endblock %}
&lt;p&gt;Dear &lt;span class="variable-highlight"&gt;{{ attention }}&lt;/span&gt;,&lt;/p&gt;
&lt;p&gt;Please find attached our purchase order{% if task %} for &lt;span class="variable-highlight"&gt;{{ task.name }}&lt;/span&gt;{% endif %}.&lt;/p&gt;
&lt;p&gt;Please deliver the parts to &lt;span class="variable-highlight"&gt;{{purchaseorder.delivery_instructions}}&lt;/span&gt; &lt;/p&gt;
&lt;p&gt;&lt;strong&gt;Delivery Address:&lt;strong&gt;&lt;/p&gt;
{% endraw %}
```

```django
{% raw %}
{% for task in tasks %}
&lt;p&gt;
Task &lt;span class="variable-highlight"&gt;{{ task.ref }}&lt;/span&gt;&lt;br&gt;
&lt;span class="variable-highlight"&gt;{{ task.description }}&lt;/span&gt;&lt;br&gt;
&lt;span class="variable-highlight"&gt;{{ task.property.name }}&lt;/span&gt;&lt;br&gt;
{% endraw %}
```

```django
{% raw %}
&lt;p&gt;
Task &lt;span class="variable-highlight"&gt;{{ task.ref }}&lt;/span&gt;&lt;br&gt;
&lt;span class="variable-highlight"&gt;{{ task.description }}&lt;/span&gt;&lt;br&gt;
&lt;span class="variable-highlight"&gt;{{ task.property.name }}&lt;/span&gt;&lt;br&gt;
&lt;span class="variable-highlight"&gt;{{ task.address }}&lt;/span&gt;
{% endraw %}
```

</details>

---

## task_origin_defectquote

<details class="expandable-section">
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details class="expandable-section">
<summary><strong>Properties</strong></summary>


| Property | Example Value |
|----------|---------------|
| `status` | `{{ task_origin_defectquote.status }}` |
| `status.upper` | `{{ task_origin_defectquote.status.upper }}` |

</details>

<details>
<summary><strong>Usage Examples</strong></summary>

```django
{% raw %}
{% include "reports/library/arrow-up-right-from-square-icon.svg" with width="14" height="14" %}
&lt;/a&gt;
&lt;div class="status quote &lt;span class="variable-highlight"&gt;{{ task_origin_defectquote.status }}&lt;/span&gt; ml-2 mt-1"&gt;
&lt;span class="variable-highlight"&gt;{{ task_origin_defectquote.status.upper }}&lt;/span&gt;
&lt;/div&gt;
{% endraw %}
```

```django
{% raw %}
&lt;/a&gt;
&lt;div class="status quote &lt;span class="variable-highlight"&gt;{{ task_origin_defectquote.status }}&lt;/span&gt; ml-2 mt-1"&gt;
&lt;span class="variable-highlight"&gt;{{ task_origin_defectquote.status.upper }}&lt;/span&gt;
&lt;/div&gt;
&lt;/div&gt;
{% endraw %}
```

</details>

---

## task_quote

<details class="expandable-section">
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details class="expandable-section">
<summary><strong>Properties</strong></summary>


| Property | Example Value |
|----------|---------------|
| `get_uuid_approval_url` | `{{ task_quote.get_uuid_approval_url\|absolute }}` |
| `ref` | `{{ task_quote.ref }}` |

</details>

<details class="expandable-section">
<summary><strong>Filters Used</strong></summary>

- `absolute`

</details>

<details>
<summary><strong>Usage Examples</strong></summary>

```django
{% raw %}
{% if task_quote.ref %}
&lt;div class="subtitle d-flex flex-row"&gt;
&lt;a href="&lt;span class="variable-highlight"&gt;{{ task_quote.get_uuid_approval_url|absolute }}&lt;/span&gt;"&gt;
&lt;span class="variable-highlight"&gt;{{ task_quote.ref }}&lt;/span&gt;
{% include "reports/library/arrow-up-right-from-square-icon.svg" with width="14" height="14" %}
{% endraw %}
```

```django
{% raw %}
&lt;div class="subtitle d-flex flex-row"&gt;
&lt;a href="&lt;span class="variable-highlight"&gt;{{ task_quote.get_uuid_approval_url|absolute }}&lt;/span&gt;"&gt;
&lt;span class="variable-highlight"&gt;{{ task_quote.ref }}&lt;/span&gt;
{% include "reports/library/arrow-up-right-from-square-icon.svg" with width="14" height="14" %}
&lt;/a&gt;
{% endraw %}
```

</details>

---

## tasksession

<details class="expandable-section">
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details class="expandable-section">
<summary><strong>Properties</strong></summary>


| Property | Example Value |
|----------|---------------|
| `id` | `{{ tasksession.id }}` |
| `technician.name` | `{{ tasksession.technician.name }}` |

</details>

<details>
<summary><strong>Usage Examples</strong></summary>

```django
{% raw %}
&lt;/p&gt;
&lt;p&gt;Thanks&lt;/p&gt;
&lt;p&gt;Task Session &lt;span class="variable-highlight"&gt;{{ tasksession.id }}&lt;/span&gt; encountered an error while syncing to the accounting partner.&lt;/p&gt;
{% if task %}
&lt;p&gt;&lt;b&gt;Task:&lt;/b&gt; &lt;span class="variable-highlight"&gt;{{ task }}&lt;/span&gt;&lt;/p&gt;
{% endraw %}
```

```django
{% raw %}
&lt;p&gt;&lt;b&gt;Task:&lt;/b&gt; &lt;span class="variable-highlight"&gt;{{ task }}&lt;/span&gt;&lt;/p&gt;
{% endif %}
&lt;p&gt;&lt;b&gt;Technician:&lt;/b&gt; &lt;span class="variable-highlight"&gt;{{ tasksession.technician.name }}&lt;/span&gt;&lt;/p&gt;
&lt;p&gt;Please review and address the error, then use the link below to retry the sync&lt;/p&gt;
&lt;p&gt;
{% endraw %}
```

</details>

---

## template

<details class="expandable-section">
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details>
<summary><strong>Usage Examples</strong></summary>

```django
{% raw %}
&lt;p&gt;
Change request: &lt;a href="&lt;span class="variable-highlight"&gt;{{ base_url }}&lt;/span&gt;&lt;span class="variable-highlight"&gt;{{ changerequest.get_absolute_url }}&lt;/span&gt;"&gt;&lt;span class="variable-highlight"&gt;{{ changerequest.ref }}&lt;/span&gt;&lt;/a&gt;&lt;br /&gt;
Template: {% if template %}&lt;span class="variable-highlight"&gt;{{ template }}&lt;/span&gt;{% else %}New Template{% endif %}&lt;br /&gt;
Status: &lt;span class="variable-highlight"&gt;{{ changerequest.status }}&lt;/span&gt;
&lt;/p&gt;&lt;p&gt;Dear &lt;span class="variable-highlight"&gt;{{ client.name|default:'valued customer' }}&lt;/span&gt;,&lt;/p&gt;
{% endraw %}
```

</details>

---

## title

<details class="expandable-section">
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details>
<summary><strong>Usage Examples</strong></summary>

```django
{% raw %}
&lt;div&gt;
&lt;div class="uptick-heading d-flex flex-row justify-content-between w-100 no-page-break-after"&gt;
&lt;div&gt;&lt;span class="variable-highlight"&gt;{{ title }}&lt;/span&gt;&lt;/div&gt;
{% if task_quote.ref %}
&lt;div class="subtitle d-flex flex-row"&gt;
{% endraw %}
```

</details>

---

## to_list

<details class="expandable-section">
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details>
<summary><strong>Usage Examples</strong></summary>

```django
{% raw %}
Email info:&lt;br /&gt;
Sent: &lt;span class="variable-highlight"&gt;{{ failure_datetime }}&lt;/span&gt;&lt;br /&gt;
To: &lt;span class="variable-highlight"&gt;{{ to_list }}&lt;/span&gt;&lt;br /&gt;
CC: &lt;span class="variable-highlight"&gt;{{ cc_list }}&lt;/span&gt;&lt;br /&gt;
Subject &lt;span class="variable-highlight"&gt;{{ subject }}&lt;/span&gt;&lt;br /&gt;
{% endraw %}
```

</details>

---

## url

<details class="expandable-section">
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details>
<summary><strong>Usage Examples</strong></summary>

```django
{% raw %}
&lt;p&gt;A new message from &lt;span class="variable-highlight"&gt;{{ from }}&lt;/span&gt; is waiting for you:&lt;/p&gt;
&lt;p&gt;&lt;span class="variable-highlight"&gt;{{ chat_message.text }}&lt;/span&gt;&lt;/p&gt;
&lt;p&gt;&lt;span class="variable-highlight"&gt;{{ base_url }}&lt;/span&gt;&lt;span class="variable-highlight"&gt;{{ url }}&lt;/span&gt;&lt;/p&gt;
&lt;p&gt;Regards, &lt;br/&gt;
&lt;span class="variable-highlight"&gt;{{ config.SITE_ORGANISATION }}&lt;/span&gt;
{% endraw %}
```

</details>

---


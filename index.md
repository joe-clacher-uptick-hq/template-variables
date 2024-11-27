---
title: Django Template Variables Documentation
layout: default
---


    <!-- CSS styles remain unchanged -->
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

<details class="expandable-section">
<summary><strong>Usage Examples</strong></summary>

```django
{{ rectification.rejection_reason|markdowner }}
<p>Access the rectification to provide updated information:</p>
<p><a href="{{ base_url }}{{ absolute_url }}">{{ base_url }}{{ absolute_url }}</a></p>
{% endblock %}
{% extends 'email.html' %}
```

</details>

---

## approved_by

<details class="expandable-section">
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details class="expandable-section">
<summary><strong>Usage Examples</strong></summary>

```django
</p>
<p>
  The service quote for {{ property }} was approved by {{ approved_by }}.
</p>
<p>
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
| `scheduled_start` | `{%raw%}{{appt.scheduled_start}}{%endraw%}` |
| `task.authorisation_ref` | `{%raw%}{{appt.task.authorisation_ref}}{%endraw%}` |
| `task.description` | `{%raw%}{{appt.task.description}}{%endraw%}` |
| `task.name` | `{%raw%}{{appt.task.name}}{%endraw%}` |
| `task.property.name` | `{%raw%}{{appt.task.property.name}}{%endraw%}` |
| `task.ref` | `{%raw%}{{appt.task.ref}}{%endraw%}` |
| `task.scope_of_works` | `{%raw%}{{appt.task.scope_of_works}}{%endraw%}` |
| `technicians.first` | `{%raw%}{{appt.technicians.first}}{%endraw%}` |

</details>

<details class="expandable-section">
<summary><strong>Usage Examples</strong></summary>

```django
{% timezone tmz %}
                        <tr>
                          <th style="padding: 12px 10px; border-top: 1px solid #dcdddd;" scope="row" colspan="4">{{appt.scheduled_start}}</th>
                          <td style="padding: 12px 10px; border-top: 1px solid #dcdddd;">{{appt.task.description}}</td>
                          <td style="padding: 12px 10px; border-top: 1px solid #dcdddd;">{{appt.task.property.name}}</td>
```

```django
<tr>
                          <th style="padding: 12px 10px; border-top: 1px solid #dcdddd;" scope="row" colspan="4">{{appt.scheduled_start}}</th>
                          <td style="padding: 12px 10px; border-top: 1px solid #dcdddd;">{{appt.task.description}}</td>
                          <td style="padding: 12px 10px; border-top: 1px solid #dcdddd;">{{appt.task.property.name}}</td>
                          <td style="padding: 12px 10px; border-top: 1px solid #dcdddd;">{{appt.task.scope_of_works}}</td>
```

```django
<th style="padding: 12px 10px; border-top: 1px solid #dcdddd;" scope="row" colspan="4">{{appt.scheduled_start}}</th>
                          <td style="padding: 12px 10px; border-top: 1px solid #dcdddd;">{{appt.task.description}}</td>
                          <td style="padding: 12px 10px; border-top: 1px solid #dcdddd;">{{appt.task.property.name}}</td>
                          <td style="padding: 12px 10px; border-top: 1px solid #dcdddd;">{{appt.task.scope_of_works}}</td>
                          <td style="padding: 12px 10px; border-top: 1px solid #dcdddd;">{{appt.task.authorisation_ref}}</td>
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

<details class="expandable-section">
<summary><strong>Usage Examples</strong></summary>

```django
<td style="width: 600px;">
            <div style="font-family: 'Arial', sans-serif; font-size: 10.5pt;">
                <p style="padding: 10px 0;">Dear {{ attention }},</p>
                <p>Please be advised we will need access to complete the following:</p>
                <table style="width: 100%; border-collapse: collapse; border-bottom: 1px solid #dcdddd;">
```

```django
</table>
{% endblock %}
<p>Dear {{ attention }},</p>
<p>Please find attached your defect quote for {{ property.name }}.</p>
<p>To view and approve this quote online, visit:</p>
```

```django
<p>Regards,<br />
{{ config.SITE_ORGANISATION }}</p>
<p>Dear {{ attention|default:"manager" }},</p>
<p>Please find attached your documents for services recently carried out at {{ property.name }}.</p>
{% if invoice %}
```

</details>

---

## base_url

<details class="expandable-section">
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details class="expandable-section">
<summary><strong>Usage Examples</strong></summary>

```django
<p>Please find attached your defect quote for {{ property.name }}.</p>
<p>To view and approve this quote online, visit:</p>
<p><a href="{{ base_url }}{{ quote.get_uuid_approval_url }}">{{ base_url }}{{ quote.get_uuid_approval_url }}</a></p>
<p>We value your opinion, please contact us with any comments you may have.</p>
<p>Regards,<br />
```

```django
<ul>
    {% for quote in defectquotes %}
      <li>Reference: {{ quote.ref }}<a href="{{ base_url }}{{ quote.get_uuid_approval_url }}"> (approve online)</a></li>
    {% endfor %}
  </ul>
```

```django
<p>
  Please go to this URL to set your password and start using Uptick:
  {{ base_url }}{% url 'password_reset_confirm' uidb64=uid token=token %}
</p>
{% if account.license == "FIELD" %}
```

</details>

---

## bounce_address

<details class="expandable-section">
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details class="expandable-section">
<summary><strong>Usage Examples</strong></summary>

```django
<p>
  Bounce info:<br />
  Address: {{ bounce_address }}<br />
  Bounce Reason: {{ formatted_reason }}<br />
  Email Subject {{ subject }}<br />
```

</details>

---

## cc_list

<details class="expandable-section">
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details class="expandable-section">
<summary><strong>Usage Examples</strong></summary>

```django
Sent: {{ failure_datetime }}<br />
  To: {{ to_list }}<br />
  CC: {{ cc_list }}<br />
  Subject {{ subject }}<br />
</p>
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
| `get_absolute_url` | `{%raw%}{{ changerequest.get_absolute_url }}{%endraw%}` |
| `ref` | `{%raw%}{{ changerequest.ref }}{%endraw%}` |
| `status` | `{%raw%}{{ changerequest.status }}{%endraw%}` |

</details>

<details class="expandable-section">
<summary><strong>Usage Examples</strong></summary>

```django
{{ config.SITE_ORGANISATION }}</p>
{% if status == 'DRAFT' %}
  <p>Template change request {{ changerequest.ref }} has been created for {{ customer }}.</p>
{% elif  status == 'REQUESTED' %}
  <p>{{ sender.name }} submitted feedback for Template change request {{ changerequest.ref }}.</p>
```

```django
<p>Template change request {{ changerequest.ref }} has been created for {{ customer }}.</p>
{% elif  status == 'REQUESTED' %}
  <p>{{ sender.name }} submitted feedback for Template change request {{ changerequest.ref }}.</p>
{% else %}
  <p>Template change request {{ changerequest.ref }} has been approved. Our team will be in contact once completed.</p>
```

```django
<p>{{ sender.name }} submitted feedback for Template change request {{ changerequest.ref }}.</p>
{% else %}
  <p>Template change request {{ changerequest.ref }} has been approved. Our team will be in contact once completed.</p>
{% endif %}
<p>
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
| `text` | `{%raw%}{{ chat_message.text }}{%endraw%}` |

</details>

<details class="expandable-section">
<summary><strong>Usage Examples</strong></summary>

```django
</p>
<p>A new message from {{ from }} is waiting for you:</p>
<p>{{ chat_message.text }}</p>
<p>{{ base_url }}{{ url }}</p>
<p>Regards, <br/>
```

```django
{% endblock %}
<p>A new message from {{ from }} is waiting for you:</p>
<p>{{ chat_message.text }}</p>
<p>{{ base_url }}{{ url }}</p>
<p>Regards, <br/>
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
| `primary_contact.name` | `{%raw%}{{ client.primary_contact.name }}{%endraw%}` |

</details>

<details class="expandable-section">
<summary><strong>Usage Examples</strong></summary>

```django
<p>If the form{{ signoffproperties|pluralize }} on the attached link {{ signoffproperties|pluralize:"is,are" }} not submitted and there is no proof on site that the Essential Safety Measures are being serviced, {{ signoffproperties|pluralize:"a," }} Non-Compliant Building Report{{ signoffproperties|pluralize }} will be issued.</p>
{% endblock %}
<p>Dear {{ client.primary_contact.name }},</p>
<p>This email is in regards to your property {{ property.ref }} {{ property.name }} {{ property.client_ref }}.</p>
<p>We have received notification from {{ contractor.name }} that they are no longer engaged to maintain the following items:</p>
```

```django
<div>{{ servicequote.created|date:"jS F Y" }}</div>
    {% if servicequote.expiry_date %}<div>This quote is valid until <em>{{ servicequote.expiry_date }}</em></div>{% endif %}
    <div><strong>Attention: {{ client.primary_contact.name }}</strong></div>
    {% if servicequote.scope_of_works %}
      <div class="mt-3">
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
| `CONTACT_EMAIL` | `{%raw%}{{ config.CONTACT_EMAIL }}{%endraw%}` |
| `CONTACT_PHONE` | `{%raw%}{{config.CONTACT_PHONE}}{%endraw%}` |
| `SITE_ORGANISATION` | `{%raw%}{{config.SITE_ORGANISATION}}{%endraw%}` |

</details>

<details class="expandable-section">
<summary><strong>Usage Examples</strong></summary>

```django
<p>{{request_user.email}}</p>
                <p>
                  {{ config.CONTACT_PHONE }} <br />
                  {{ config.SITE_ORGANISATION }}
                </p>
```

```django
<p>
                  {{ config.CONTACT_PHONE }} <br />
                  {{ config.SITE_ORGANISATION }}
                </p>
            </div>
```

```django
<p>We value your opinion, please contact us with any comments you may have.</p>
<p>Regards,<br />
{{ config.SITE_ORGANISATION }}</p>
<p>Dear {{ attention|default:"manager" }},</p>
<p>Please find attached your documents for services recently carried out at {{ property.name }}.</p>
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
| `account` | `{%raw%}{{ contractor.account }}{%endraw%}` |
| `name` | `{%raw%}{{ contractor.name }}{%endraw%}` |

</details>

<details class="expandable-section">
<summary><strong>Usage Examples</strong></summary>

```django
{{ config.SITE_ORGANISATION }}</p>
{% endblock %}
<p>Dear {{ contractor }},</p>
<p>You have been assigned the following tasks:</p>
{% for task in tasks %}
```

```django
<p>You can provide your field technicians with this link which will enable them to complete the task via their smart phone (apple or android) without needing to install an app.</p>
<p>Thanks</p>
<p>The contractor {{ contractor }} has rejected the task assigned to him for the following reason: {{ rejection_reason }}</p>
<p>
  The task that was assigned was:<br>
```

```django
</p>
<p>Thanks</p>
<p>Dear {{ contractor }},</p>
<p>Please be advised that the following task has been cancelled:</p>
<ul>
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
| `name` | `{%raw%}{{ contractor_contact.name }}{%endraw%}` |

</details>

<details class="expandable-section">
<summary><strong>Usage Examples</strong></summary>

```django
<p>Regards,<br/>
{{ config.SITE_ORGANISATION }}</p>
<p>Dear {{ contractor_contact }},</p>
<p>Please be advised that the following task has been cancelled:</p>
<ul>
```

```django
{{ config.SITE_ORGANISATION }}
</p>
<p>Dear {{ contractor_contact.name }},</p>
<p>You have been assigned a task:</p>
<p>Task {{ task.ref }}</p>
```

```django
</p>
<p>Thanks</p>
<p>Dear {{ contractor_contact.name }},</p>
<p>You have been assigned the following tasks:</p>
{% for task in tasks %}
```

</details>

---

## contractor_login_url

<details class="expandable-section">
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details class="expandable-section">
<summary><strong>Usage Examples</strong></summary>

```django
<p>
  Please sign in the contractor portal using the link below to view a list of any outstanding tasks:<br>
  <a href="{{ contractor_login_url }}">{{ contractor_login_url }}</a>
</p>
<p>You can provide your field technicians with this link which will enable them to complete the task via their smart phone (apple or android) without needing to install an app.</p>
```

```django
<p>
  Please visit the task dashboard on Uptick:<br>
  <a href="{{ contractor_login_url }}">{{ contractor_login_url }}</a><br>
  for more details.
</p>
```

```django
<p>{{ task.address }}</p>
<p>Please sign into the contractor portal using the link below to view your outstanding tasks:<br>
  <a href="{{ contractor_login_url }}">{{ contractor_login_url }}</a>
</p>
<p>Thanks</p>
```

</details>

---

## csv_url

<details class="expandable-section">
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details class="expandable-section">
<summary><strong>Usage Examples</strong></summary>

```django
<p>Your custom report, {{ name }}, has been generated.</p>
<p>{{ description }}</p>
<p>To download, <a href="{{ csv_url }}">please click here</a>.</p>
{% endblock %}
<p>Dear {{ attention }},</p>
```

</details>

---

## custom_message

<details class="expandable-section">
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details class="expandable-section">
<summary><strong>Usage Examples</strong></summary>

```django
{% if custom_message %}
<p>
  {{ custom_message }}
</p>
{% endif %}
```

</details>

---

## customer

<details class="expandable-section">
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details class="expandable-section">
<summary><strong>Usage Examples</strong></summary>

```django
{{ config.SITE_ORGANISATION }}</p>
{% if status == 'DRAFT' %}
  <p>Template change request {{ changerequest.ref }} has been created for {{ customer }}.</p>
{% elif  status == 'REQUESTED' %}
  <p>{{ sender.name }} submitted feedback for Template change request {{ changerequest.ref }}.</p>
```

</details>

---

## declined_by

<details class="expandable-section">
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details class="expandable-section">
<summary><strong>Usage Examples</strong></summary>

```django
</p>
<p>
  The service quote for {{ property }} was declined by {{ declined_by }}.
</p>
<p>
```

</details>

---

## description

<details class="expandable-section">
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details class="expandable-section">
<summary><strong>Usage Examples</strong></summary>

```django
{% block content %}
<p>Your custom report, {{ name }}, has been generated.</p>
<p>{{ description }}</p>
<p>To download, <a href="{{ csv_url }}">please click here</a>.</p>
{% endblock %}
```

</details>

---

## email
<div class="loop-info">Loop Iterator<span class="tooltip">This variable represents a single item from a list or collection being looped over.</span></div>

<details class="expandable-section">
<summary><strong>Found in files</strong></summary>

- generic.txt

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

## end_date

<details class="expandable-section">
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details class="expandable-section">
<summary><strong>Usage Examples</strong></summary>

```django
<td style="border: 3px double #000; padding: 8px; width: 25%;">{{start_date}}</td>
                        <td style="border: 3px double #000; padding: 8px; width: 25%; background-color: #f0f0f0;">END DATE</td>
                        <td style="border: 3px double #000; padding: 8px; width: 25%;">{{end_date}}</td>
                    </tr>
                    <tr>
```

</details>

---

## exception

<details class="expandable-section">
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details class="expandable-section">
<summary><strong>Usage Examples</strong></summary>

```django
</p>
<h3>Error</h3>
<code>{{ exception }}</code>
<p>
  An email failed to send from Uptick! This is sometimes due to an invalid email, but more details below.
```

</details>

---

## failure_datetime

<details class="expandable-section">
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details class="expandable-section">
<summary><strong>Usage Examples</strong></summary>

```django
<p>
  Email info:<br />
  Sent: {{ failure_datetime }}<br />
  To: {{ to_list }}<br />
  CC: {{ cc_list }}<br />
```

</details>

---

## failure_reason

<details class="expandable-section">
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details class="expandable-section">
<summary><strong>Usage Examples</strong></summary>

```django
An email failed to send from Uptick! This is sometimes due to an invalid email, but more details below.
  <br />
  {{ failure_reason }}
</p>
<p>
```

</details>

---

## formatted_reason

<details class="expandable-section">
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details class="expandable-section">
<summary><strong>Usage Examples</strong></summary>

```django
Bounce info:<br />
  Address: {{ bounce_address }}<br />
  Bounce Reason: {{ formatted_reason }}<br />
  Email Subject {{ subject }}<br />
  Email Sent: {{ formatted_timestamp }}
```

</details>

---

## formatted_timestamp

<details class="expandable-section">
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details class="expandable-section">
<summary><strong>Usage Examples</strong></summary>

```django
Bounce Reason: {{ formatted_reason }}<br />
  Email Subject {{ subject }}<br />
  Email Sent: {{ formatted_timestamp }}
</p>
<p>
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
| `submitter` | `{%raw%}{{ formresponse.submitter }}{%endraw%}` |
| `template_version.template.name` | `{%raw%}{{ formresponse.template_version.template.name }}{%endraw%}` |

</details>

<details class="expandable-section">
<summary><strong>Usage Examples</strong></summary>

```django
<ul>
  {% for formresponse in formresponses %}
    <li>{{ formresponse }}</li>
  {% endfor %}
</ul>
```

```django
</p><p>Dear {{ attention }},</p>
<p>Please find attached a form response regarding work at {{ property.name }}.</p>
<p>Form: {{ formresponse.template_version.template.name }}</p>
<p>Submitted by: {{ formresponse.submitter }}</p>
<p>We value your opinion, please contact us with any comments you may have.</p>
```

```django
<p>Please find attached a form response regarding work at {{ property.name }}.</p>
<p>Form: {{ formresponse.template_version.template.name }}</p>
<p>Submitted by: {{ formresponse.submitter }}</p>
<p>We value your opinion, please contact us with any comments you may have.</p>
<p>Regards,<br />
```

</details>

---

## from

<details class="expandable-section">
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details class="expandable-section">
<summary><strong>Usage Examples</strong></summary>

```django
{{ config.SITE_ORGANISATION }}
</p>
<p>A new message from {{ from }} is waiting for you:</p>
<p>{{ chat_message.text }}</p>
<p>{{ base_url }}{{ url }}</p>
```

```django
{% endfor %}
{% endblock %}
<p>A new message from {{ from }} is waiting for you:</p>
<p>{{ chat_message.text }}</p>
<p>{{ base_url }}{{ url }}</p>
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
| `number` | `{%raw%}{{ inv.number }}{%endraw%}` |
| `ref` | `{%raw%}{{ inv.ref }}{%endraw%}` |

</details>

<details class="expandable-section">
<summary><strong>Usage Examples</strong></summary>

```django
<p>This is a reminder that we are waiting for your payment on the following invoices:<br>
{% for inv in invoices %}<br>
    Number: {{ inv.number }}<br>
    Reference: {{ inv.ref }}<br>
    Due: {{ inv.due_date|date:"jS F Y" }}<br>
```

```django
{% for inv in invoices %}<br>
    Number: {{ inv.number }}<br>
    Reference: {{ inv.ref }}<br>
    Due: {{ inv.due_date|date:"jS F Y" }}<br>
{% endfor %}
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
| `ref` | `{%raw%}{{ invoice.ref }}{%endraw%}` |

</details>

<details class="expandable-section">
<summary><strong>Usage Examples</strong></summary>

```django
<p>Your invoice:</p>
  <ul>
    <li>{{ invoice.number|default:"[[ invoice_number ]]" }} {% if invoice.ref %}({{ invoice.ref }}){% endif %}</li>
  </ul>
{% endif %}
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
| `label` | `{%raw%}{{ item.label }}{%endraw%}` |

</details>

<details class="expandable-section">
<summary><strong>Usage Examples</strong></summary>

```django
<ul>
    {% for item in items %}
    <li>{{ item.label }}</li>
    {% endfor %}
</ul>
```

</details>

---

## lead_engineer

<details class="expandable-section">
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details class="expandable-section">
<summary><strong>Usage Examples</strong></summary>

```django
<tr>
                        <td style="border: 3px double #000; padding: 8px; background-color: #f0f0f0;">LEAD ENGINEER</td>
                        <td style="border: 3px double #000; padding: 8px;" colspan="3">{{lead_engineer}}</td>
                    </tr>
                    <tr>
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
| `annual_subtotal` | `{%raw%}{{ line.annual_subtotal\|currency }}{%endraw%}` |
| `product.name` | `{%raw%}{{ line.product.name }}{%endraw%}` |
| `quantity` | `{%raw%}{{ line.quantity\|floatformat:2 }}{%endraw%}` |
| `routineservicetype.name` | `{%raw%}{{ line.routineservicetype.name }}{%endraw%}` |
| `site_price` | `{%raw%}{{ line.site_price\|currency }}{%endraw%}` |
| `subtotal` | `{%raw%}{{ line.subtotal\|currency }}{%endraw%}` |
| `unit_price` | `{%raw%}{{ line.unit_price\|currency }}{%endraw%}` |

</details>

<details class="expandable-section">
<summary><strong>Filters Used</strong></summary>

- `currency`
- `floatformat (arg: 2)`

</details>

<details class="expandable-section">
<summary><strong>Usage Examples</strong></summary>

```django
<tr class="keep-together">
              <td>
                <div>{{ line.product.name }}</div>
                <div class="text-muted">{{ line.description|default:'-' }}</div>
              </td>
```

```django
<div class="text-muted">{{ line.description|default:'-' }}</div>
              </td>
              <td class="text-right">{{ line.quantity|floatformat:2 }}</td>
              <td class="text-right">{{ line.unit_price|currency }}</td>
              <td class="text-right">{{ line.subtotal|currency }}</td>
```

```django
</td>
              <td class="text-right">{{ line.quantity|floatformat:2 }}</td>
              <td class="text-right">{{ line.unit_price|currency }}</td>
              <td class="text-right">{{ line.subtotal|currency }}</td>
            </tr>
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
| `name` | `{%raw%}{{ logbook.name }}{%endraw%}` |

</details>

<details class="expandable-section">
<summary><strong>Usage Examples</strong></summary>

```django
<ul>
  {% for logbook in digital_logbooks %}
    <li>{{ logbook.name }}</li>
  {% endfor %}
</ul>
```

</details>

---

## login_url

<details class="expandable-section">
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details class="expandable-section">
<summary><strong>Usage Examples</strong></summary>

```django
<tr>
  <td align="center" bgcolor="#27a9e3">
    <a style="color: white; text-decoration: underline;" href="{{ login_url }}">
      Open your contractor portal
    </a>
```

</details>

---

## message

<details class="expandable-section">
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details class="expandable-section">
<summary><strong>Usage Examples</strong></summary>

```django
{% endblock %}
<p>A webhook event from Corrigo was rejected.</p>
<p>Reason: {{ message }}</p>
<p>Payload:<p>
<pre><code>{{payload}}</code></pre>
```

```django
{{ property_refs|join:", " }}
      <br />
      {{ message }}
    </li>
  </ul>
```

</details>

---

## name

<details class="expandable-section">
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details class="expandable-section">
<summary><strong>Usage Examples</strong></summary>

```django
\{% extends 'email.html' %}
{% block content %}
<p>Your custom report, {{ name }}, has been generated.</p>
<p>{{ description }}</p>
<p>To download, <a href="{{ csv_url }}">please click here</a>.</p>
```

</details>

---

## no_of_assets

<details class="expandable-section">
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details class="expandable-section">
<summary><strong>Usage Examples</strong></summary>

```django
<p>Regards,<br />
Uptick Team</p>
<p>There are currently {{ no_of_assets }} assets not covered by any Routines. These assets relate to the following properties:</p>
<ul>
{% for property in properties %}
```

</details>

---

## payload

<details class="expandable-section">
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details class="expandable-section">
<summary><strong>Usage Examples</strong></summary>

```django
<p>Reason: {{ message }}</p>
<p>Payload:<p>
<pre><code>{{payload}}</code></pre>
<p>Regards,<br />
Uptick Team</p>
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
| `name` | `{%raw%}{{ promptset.name }}{%endraw%}` |
| `ref` | `{%raw%}{{ promptset.ref }}{%endraw%}` |

</details>

<details class="expandable-section">
<summary><strong>Usage Examples</strong></summary>

```django
<tr>
                            <th colspan="3" class="border-top-0">
                              ({{ promptset.ref }}) {{ promptset.name }}
                            </th>
                          </tr>
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
| `client_ref` | `{%raw%}{{ property.client_ref }}{%endraw%}` |
| `name` | `{%raw%}{{ property.name }}{%endraw%}` |
| `property__name` | `{%raw%}{{ property.property__name }}{%endraw%}` |
| `property_id` | `{%raw%}{{property.property_id}}{%endraw%}` |
| `ref` | `{%raw%}{{ property.ref }}{%endraw%}` |

</details>

<details class="expandable-section">
<summary><strong>Usage Examples</strong></summary>

```django
{% endblock %}
<p>Dear {{ attention }},</p>
<p>Please find attached your defect quote for {{ property.name }}.</p>
<p>To view and approve this quote online, visit:</p>
<p><a href="{{ base_url }}{{ quote.get_uuid_approval_url }}">{{ base_url }}{{ quote.get_uuid_approval_url }}</a></p>
```

```django
{{ config.SITE_ORGANISATION }}</p>
<p>Dear {{ attention|default:"manager" }},</p>
<p>Please find attached your documents for services recently carried out at {{ property.name }}.</p>
{% if invoice %}
  <p>Your invoice:</p>
```

```django
<p>For any questions, please contact us.</p>
<p>Dear {{ attention|default:"manager" }},</p>
<p>Please find attached your documents for services recently carried out at {{ property.name }}.</p>
{% if invoice %}
  <p>Your invoice:</p>
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
| `delivery_instructions` | `{%raw%}{{purchaseorder.delivery_instructions}}{%endraw%}` |

</details>

<details class="expandable-section">
<summary><strong>Usage Examples</strong></summary>

```django
<p>Dear {{ attention }},</p>
<p>Please find attached our purchase order{% if task %} for {{ task.name }}{% endif %}.</p>
<p>Please deliver the parts to {{purchaseorder.delivery_instructions}} </p>
<p><strong>Delivery Address:<strong></p>
<p>Regards,<br />
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
| `get_uuid_approval_url` | `{%raw%}{{ quote.get_uuid_approval_url }}{%endraw%}` |
| `property.name` | `{%raw%}{{ quote.property.name }}{%endraw%}` |
| `ref` | `{%raw%}{{ quote.ref }}{%endraw%}` |
| `status.upper` | `{%raw%}{{ quote.status.upper }}{%endraw%}` |

</details>

<details class="expandable-section">
<summary><strong>Filters Used</strong></summary>

- `absolute`

</details>

<details class="expandable-section">
<summary><strong>Usage Examples</strong></summary>

```django
<p>Please find attached your defect quote for {{ property.name }}.</p>
<p>To view and approve this quote online, visit:</p>
<p><a href="{{ base_url }}{{ quote.get_uuid_approval_url }}">{{ base_url }}{{ quote.get_uuid_approval_url }}</a></p>
<p>We value your opinion, please contact us with any comments you may have.</p>
<p>Regards,<br />
```

```django
<ul>
    {% for quote in defectquotes %}
      <li>Reference: {{ quote.ref }}<a href="{{ base_url }}{{ quote.get_uuid_approval_url }}"> (approve online)</a></li>
    {% endfor %}
  </ul>
```

```django
{% endif %}
<p>To view and approve this quote online, visit:</p>
<p><a href="{{ base_url }}{{ quote.get_uuid_approval_url }}">{{ base_url }}{{ quote.get_uuid_approval_url }}</a></p>
<p>Regards,<br />
{{ config.SITE_ORGANISATION }}</p>
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
| `ref` | `{%raw%}{{ rectification.ref }}{%endraw%}` |
| `rejection_reason` | `{%raw%}{{ rectification.rejection_reason\|markdowner }}{%endraw%}` |

</details>

<details class="expandable-section">
<summary><strong>Filters Used</strong></summary>

- `markdowner`

</details>

<details class="expandable-section">
<summary><strong>Usage Examples</strong></summary>

```django
{% load markdowner %}
{% block content %}
<h4>Rectification {{ rectification.ref }} was rejected.</h4>
<p>Reason provided:</p>
{{ rectification.rejection_reason|markdowner }}
```

```django
<h4>Rectification {{ rectification.ref }} was rejected.</h4>
<p>Reason provided:</p>
{{ rectification.rejection_reason|markdowner }}
<p>Access the rectification to provide updated information:</p>
<p><a href="{{ base_url }}{{ absolute_url }}">{{ base_url }}{{ absolute_url }}</a></p>
```

</details>

---

## ref_no

<details class="expandable-section">
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details class="expandable-section">
<summary><strong>Usage Examples</strong></summary>

```django
<tr>
                        <td style="border: 3px double #000; padding: 8px; background-color: #f0f0f0;">OUR REF NO.</td>
                        <td style="border: 3px double #000; padding: 8px;" colspan="3">{{ref_no}}</td>
                    </tr>
                    <tr>
```

```django
<tr>
                        <td style="border: 3px double #000; padding: 8px; background-color: #f0f0f0;">VISIT No.</td>
                        <td style="border: 3px double #000; padding: 8px;" colspan="3">{{ref_no}}</td>
                    </tr>
                    <tr>
```

</details>

---

## rejection_reason

<details class="expandable-section">
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details class="expandable-section">
<summary><strong>Usage Examples</strong></summary>

```django
<p>You can provide your field technicians with this link which will enable them to complete the task via their smart phone (apple or android) without needing to install an app.</p>
<p>Thanks</p>
<p>The contractor {{ contractor }} has rejected the task assigned to him for the following reason: {{ rejection_reason }}</p>
<p>
  The task that was assigned was:<br>
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
| `get_description` | `{%raw%}{{ remark.get_description\|markdowner }}{%endraw%}` |
| `get_public_url` | `{%raw%}{{ remark.get_public_url }}{%endraw%}` |
| `get_resolution` | `{%raw%}{{ remark.get_resolution\|markdowner }}{%endraw%}` |
| `get_severity_display` | `{%raw%}{{ remark.get_severity_display }}{%endraw%}` |
| `id` | `{%raw%}{{ remark.id }}{%endraw%}` |
| `identified` | `{%raw%}{{ remark.identified }}{%endraw%}` |
| `last_verified_date` | `{%raw%}{{ remark.last_verified_date }}{%endraw%}` |
| `location` | `{%raw%}{{ remark.location\|markdowner }}{%endraw%}` |
| `severity` | `{%raw%}{{ remark.severity }}{%endraw%}` |

</details>

<details class="expandable-section">
<summary><strong>Filters Used</strong></summary>

- `markdowner`

</details>

<details class="expandable-section">
<summary><strong>Usage Examples</strong></summary>

```django
<tr>
                        <td class="m-0 p-0">
                          <div id="{{ remark.id }}"
                               class="remark severity-{{ remark.severity }} keep-together">
                            <div class="d-flex flex-row justify-content-between header">
```

```django
<td class="m-0 p-0">
                          <div id="{{ remark.id }}"
                               class="remark severity-{{ remark.severity }} keep-together">
                            <div class="d-flex flex-row justify-content-between header">
                              <div class="px-3 py-2">
```

```django
<div class="d-flex flex-row justify-content-between header">
                              <div class="px-3 py-2">
                                <strong>{{ remark.get_severity_display }}</strong>
                                <br/>
                                <a href="{{ remark.get_public_url }}">
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
| `get_title` | `{%raw%}{{ report.get_title }}{%endraw%}` |

</details>

<details class="expandable-section">
<summary><strong>Usage Examples</strong></summary>

```django
<ul>
    {% for report in reports %}
      <li>{{ report.get_title }} ({{ report.compliant|yesno:"compliant,non-compliant,not applicable"}})</li>
    {% endfor %}
  </ul>
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
| `email` | `{%raw%}{{request_user.email}}{%endraw%}` |
| `name` | `{%raw%}{{request_user.name}}{%endraw%}` |

</details>

<details class="expandable-section">
<summary><strong>Usage Examples</strong></summary>

```django
</tbody>
                </table>
                <p>If you have any queries or need to change the time, please email me at <a href="mailto:{{request_user.email}}">{{request_user.email}}</a>.</p>
                <p>Regards,<br>
                {{request_user.name}}</p>
```

```django
<p>If you have any queries or need to change the time, please email me at <a href="mailto:{{request_user.email}}">{{request_user.email}}</a>.</p>
                <p>Regards,<br>
                {{request_user.name}}</p>
                <p>{{request_user.email}}</p>
                <p>
```

```django
<p>Regards,<br>
                {{request_user.name}}</p>
                <p>{{request_user.email}}</p>
                <p>
                  {{ config.CONTACT_PHONE }} <br />
```

</details>

---

## retry_link

<details class="expandable-section">
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details class="expandable-section">
<summary><strong>Usage Examples</strong></summary>

```django
<p>Please review and address the error, then use the link below to retry the sync</p>
<p>
    <a href={{ retry_link }}>Click here</a> and use the <code>POST</code> button to retry the sync.
</p>
<h3>Error</h3>
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
| `get_routine_display_name` | `{%raw%}{{ routineserviceleveltype.get_routine_display_name }}{%endraw%}` |
| `routineservicetype.standard.name` | `{%raw%}{{ routineserviceleveltype.routineservicetype.standard.name }}{%endraw%}` |

</details>

<details class="expandable-section">
<summary><strong>Usage Examples</strong></summary>

```django
{% for routineserviceleveltype, servicetask_group in servicetasks_grouped_by_type %}
      <div class="uptick-title no-page-break-after">
        <div>{{ routineserviceleveltype.get_routine_display_name }}</div>
        {% if routineserviceleveltype.routineservicetype.standard.name != "Default" %}
          <div className="text-muted"><small>{{ routineserviceleveltype.routineservicetype.standard.name }}</small></div>
```

```django
<div>{{ routineserviceleveltype.get_routine_display_name }}</div>
        {% if routineserviceleveltype.routineservicetype.standard.name != "Default" %}
          <div className="text-muted"><small>{{ routineserviceleveltype.routineservicetype.standard.name }}</small></div>
        {% endif %}
      </div>
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
| `name` | `{%raw%}{{ rslt.name }}{%endraw%}` |

</details>

<details class="expandable-section">
<summary><strong>Usage Examples</strong></summary>

```django
{{ line.routineservicetype.name }} –
                    {% for rslt in line.routineserviceleveltypes.all %}
                      <span>{{ rslt.name }}{% if not forloop.last %}, {% endif %}</span>
                    {% endfor %}
                  </div>
```

```django
<div>{{ line.routineservicetype.name }}</div>
                  {% for rslt in line.routineserviceleveltypes.all %}
                    <span>{{ rslt.name }}{% if not forloop.last %},{% endif %}</span>
                  {% endfor %}
                </div>
```

</details>

---

## scope_of_works

<details class="expandable-section">
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details class="expandable-section">
<summary><strong>Usage Examples</strong></summary>

```django
<tr>
                        <td style="border: 3px double #000; padding: 8px; background-color: #f0f0f0;">SCOPE OF WORKS</td>
                        <td style="border: 3px double #000; padding: 8px;" colspan="3">{{scope_of_works}}</td>
                    </tr>
                </table>
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
| `name` | `{%raw%}{{ sender.name }}{%endraw%}` |

</details>

<details class="expandable-section">
<summary><strong>Usage Examples</strong></summary>

```django
<p>Template change request {{ changerequest.ref }} has been created for {{ customer }}.</p>
{% elif  status == 'REQUESTED' %}
  <p>{{ sender.name }} submitted feedback for Template change request {{ changerequest.ref }}.</p>
{% else %}
  <p>Template change request {{ changerequest.ref }} has been approved. Our team will be in contact once completed.</p>
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
| `annual_gst` | `{%raw%}{{ servicequote.annual_gst\|currency }}{%endraw%}` |
| `annual_subtotal` | `{%raw%}{{ servicequote.annual_subtotal\|currency }}{%endraw%}` |
| `annual_total` | `{%raw%}{{ servicequote.annual_total\|currency }}{%endraw%}` |
| `description` | `{%raw%}{{ servicequote.description }}{%endraw%}` |
| `expiry_date` | `{%raw%}{{ servicequote.expiry_date }}{%endraw%}` |
| `get_absolute_url` | `{%raw%}{{ servicequote.get_absolute_url }}{%endraw%}` |
| `product_gst` | `{%raw%}{{ servicequote.product_gst\|currency }}{%endraw%}` |
| `product_subtotal` | `{%raw%}{{ servicequote.product_subtotal\|currency }}{%endraw%}` |
| `product_total` | `{%raw%}{{ servicequote.product_total\|currency }}{%endraw%}` |
| `ref` | `{%raw%}{{ servicequote.ref }}{%endraw%}` |
| `salesperson.email` | `{%raw%}{{ servicequote.salesperson.email }}{%endraw%}` |
| `salesperson.name` | `{%raw%}{{ servicequote.salesperson.name }}{%endraw%}` |
| `scope_of_works` | `{%raw%}{{ servicequote.scope_of_works\|markdowner }}{%endraw%}` |
| `terms_and_conditions` | `{%raw%}{{ servicequote.terms_and_conditions\|markdowner }}{%endraw%}` |

</details>

<details class="expandable-section">
<summary><strong>Filters Used</strong></summary>

- `currency`
- `markdowner`

</details>

<details class="expandable-section">
<summary><strong>Usage Examples</strong></summary>

```django
<div>
  <strong>Scope of works:</strong>
  {{ servicequote.description }}
</div>
<br />
```

```django
Kind regards,<br /><br />
{% if servicequote.salesperson %}
<div>{{ servicequote.salesperson.name }}</div>
<div>{{ servicequote.salesperson.email }}</div>
{% endif %}
```

```django
{% if servicequote.salesperson %}
<div>{{ servicequote.salesperson.name }}</div>
<div>{{ servicequote.salesperson.email }}</div>
{% endif %}
<p>{{ config.SITE_ORGANISATION }}</p>
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
| `get_result_display.upper` | `{%raw%}{{ servicetask.get_result_display.upper }}{%endraw%}` |
| `item` | `{%raw%}{{ servicetask.item\|bsecure_url }}{%endraw%}` |
| `item.extra_fields.door_depth` | `{%raw%}{{servicetask.item.extra_fields.door_depth}}{%endraw%}` |
| `item.extra_fields.door_width` | `{%raw%}{{servicetask.item.extra_fields.door_width}}{%endraw%}` |
| `item.get_extra_fields_display.certification_id_present` | `{%raw%}{{servicetask.item.get_extra_fields_display.certification_id_present}}{%endraw%}` |
| `item.get_extra_fields_display.comments` | `{%raw%}{{servicetask.item.get_extra_fields_display.comments}}{%endraw%}` |
| `item.get_extra_fields_display.door_height` | `{%raw%}{{servicetask.item.get_extra_fields_display.door_height}}{%endraw%}` |
| `item.get_extra_fields_display.door_material` | `{%raw%}{{servicetask.item.get_extra_fields_display.door_material}}{%endraw%}` |
| `item.get_extra_fields_display.door_rating` | `{%raw%}{{servicetask.item.get_extra_fields_display.door_rating}}{%endraw%}` |
| `item.get_extra_fields_display.frame_material` | `{%raw%}{{servicetask.item.get_extra_fields_display.frame_material}}{%endraw%}` |
| `item.get_label` | `{%raw%}{{ servicetask.item.get_label }}{%endraw%}` |
| `item.inspection_ref` | `{%raw%}{{ servicetask.item.inspection_ref }}{%endraw%}` |
| `item.location` | `{%raw%}{{ servicetask.item.location }}{%endraw%}` |
| `result` | `{%raw%}{{ servicetask.result }}{%endraw%}` |

</details>

<details class="expandable-section">
<summary><strong>Filters Used</strong></summary>

- `bsecure_badge_code`
- `bsecure_url`

</details>

<details class="expandable-section">
<summary><strong>Usage Examples</strong></summary>

```django
<tbody>
            <tr class="keep-together bottom-border">
              <th width="35%" class="bg-white">{{ servicetask.item.get_label }}</th>
              <th width="50%" class="bg-white light-text-weight">
                {% if servicetask.item.inspection_ref %}
```

```django
<th width="50%" class="bg-white light-text-weight">
                {% if servicetask.item.inspection_ref %}
                  <strong>Serial:</strong> {{ servicetask.item.inspection_ref }}
                {% endif %}
                {% if servicetask.item.bsecure_latest_sticker_guid %}
```

```django
{% endif %}
                {% if servicetask.item.bsecure_latest_sticker_guid %}
                  <a href="{{ servicetask.item|bsecure_url }}">
                    <strong>BSecure:</strong> {{ servicetask.item|bsecure_badge_code }}
                    {% include "reports/library/arrow-up-right-from-square-icon.svg" with width="11" height="11" %}
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
| `account` | `{%raw%}{{ signoff.account }}{%endraw%}` |
| `contractor` | `{%raw%}{{ signoff.contractor }}{%endraw%}` |
| `period_finish` | `{%raw%}{{ signoff.period_finish }}{%endraw%}` |
| `period_start` | `{%raw%}{{ signoff.period_start}}{%endraw%}` |
| `pk` | `{%raw%}{{ signoff.pk }}{%endraw%}` |

</details>

<details class="expandable-section">
<summary><strong>Usage Examples</strong></summary>

```django
{% extends 'email.html' %}
{% block content %}
  <h3>Contractor sign off {{ signoff.pk }} results for {{ signoff.contractor }}</h3>
  <h4>Submitted by {{ signoff.account }} for {{ signoff.period_start}} to {{ signoff.period_finish }}.</h4>
  {% for signoffproperty in signoff.signoffproperty_set.all %}
```

```django
{% block content %}
  <h3>Contractor sign off {{ signoff.pk }} results for {{ signoff.contractor }}</h3>
  <h4>Submitted by {{ signoff.account }} for {{ signoff.period_start}} to {{ signoff.period_finish }}.</h4>
  {% for signoffproperty in signoff.signoffproperty_set.all %}
  <h5>{{ signoffproperty.property }}</h5>
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
| `label` | `{%raw%}{{ signoffitem.label }}{%endraw%}` |
| `new_serviced_date` | `{%raw%}{{ signoffitem.new_serviced_date }}{%endraw%}` |
| `new_signoff_note` | `{%raw%}{{ signoffitem.new_signoff_note }}{%endraw%}` |

</details>

<details class="expandable-section">
<summary><strong>Usage Examples</strong></summary>

```django
{% endif %}
      ]
      {{ signoffitem.label }}
      {% if signoffitem.new_signoff_note %}
      <div style="color: blue">Note: {{ signoffitem.new_signoff_note }}</div>
```

```django
{{ signoffitem.label }}
      {% if signoffitem.new_signoff_note %}
      <div style="color: blue">Note: {{ signoffitem.new_signoff_note }}</div>
      {% endif %}
      {% if signoffitem.new_serviced_date %}
```

```django
{% endif %}
      {% if signoffitem.new_serviced_date %}
      <div style="color: #666">Service date: {{ signoffitem.new_serviced_date }}</div>
      {% endif %}
    </li>
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

<details class="expandable-section">
<summary><strong>Usage Examples</strong></summary>

```django
{% extends 'email.html' %}
{% block content %}
<h4>Request{{ signoffproperties|pluralize }} for {{ contractor.name }} ({{ contractor.account }}).</h4>
<p>In order to issue compliant reports, we require confirmation that you, as a service contractor, have serviced the relevant Essential Safety Measures to Australian Standards over the previous 12 months.</p>
<table border="0" cellpadding="10" cellspacing="0" bgcolor="#27a9e3" width="100%">
```

```django
{% endfor %}
</ul>
<p>If the form{{ signoffproperties|pluralize }} on the attached link {{ signoffproperties|pluralize:"is,are" }} not submitted within the next 30 days and there is no proof on site that the Essential Safety Measures are being serviced, {{ signoffproperties|pluralize:"a," }} Non-Compliant Building Report{{ signoffproperties|pluralize }} will be issued.</p>
{% endblock %}
{% extends 'email.html' %}
```

```django
{% endfor %}
</ul>
<p>If the form{{ signoffproperties|pluralize }} on the attached link {{ signoffproperties|pluralize:"is,are" }} not submitted and there is no proof on site that the Essential Safety Measures are being serviced, {{ signoffproperties|pluralize:"a," }} Non-Compliant Building Report{{ signoffproperties|pluralize }} will be issued.</p>
{% endblock %}
<p>Dear {{ client.primary_contact.name }},</p>
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
| `created` | `{%raw%}{{ signoffproperty.created\|date }}{%endraw%}` |
| `disclaimed_reason` | `{%raw%}{{signoffproperty.disclaimed_reason}}{%endraw%}` |
| `due` | `{%raw%}{{ signoffproperty.due\|date }}{%endraw%}` |
| `is_disclaimed` | `{%raw%}{{ signoffproperty.is_disclaimed }}{%endraw%}` |
| `note` | `{%raw%}{{ signoffproperty.note }}{%endraw%}` |
| `property` | `{%raw%}{{ signoffproperty.property }}{%endraw%}` |
| `property.name` | `{%raw%}{{ signoffproperty.property.name }}{%endraw%}` |

</details>

<details class="expandable-section">
<summary><strong>Filters Used</strong></summary>

- `date`

</details>

<details class="expandable-section">
<summary><strong>Usage Examples</strong></summary>

```django
{% for signoffproperty in signoffproperties %}
  <li>
  <h5>{{ signoffproperty.property.name }}</h5>
  <p>
    Due: {{ signoffproperty.due|date }}
```

```django
<h5>{{ signoffproperty.property.name }}</h5>
  <p>
    Due: {{ signoffproperty.due|date }}
  </p>
  </li>
```

```django
{% for signoffproperty in signoffproperties %}
  <li>
  <h5>{{ signoffproperty.property.name }}</h5>
  <p>
    Due: {{ signoffproperty.due|date }}<br/>
```

</details>

---

## start_date

<details class="expandable-section">
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details class="expandable-section">
<summary><strong>Usage Examples</strong></summary>

```django
<tr>
                        <td style="border: 3px double #000; padding: 8px; width: 25%; background-color: #f0f0f0;">START DATE</td>
                        <td style="border: 3px double #000; padding: 8px; width: 25%;">{{start_date}}</td>
                        <td style="border: 3px double #000; padding: 8px; width: 25%; background-color: #f0f0f0;">END DATE</td>
                        <td style="border: 3px double #000; padding: 8px; width: 25%;">{{end_date}}</td>
```

</details>

---

## subject

<details class="expandable-section">
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details class="expandable-section">
<summary><strong>Usage Examples</strong></summary>

```django
To: {{ to_list }}<br />
  CC: {{ cc_list }}<br />
  Subject {{ subject }}<br />
</p>
<p>
```

```django
Address: {{ bounce_address }}<br />
  Bounce Reason: {{ formatted_reason }}<br />
  Email Subject {{ subject }}<br />
  Email Sent: {{ formatted_timestamp }}
</p>
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
| `address` | `{%raw%}{{ task.address }}{%endraw%}` |
| `description` | `{%raw%}{{ task.description }}{%endraw%}` |
| `name` | `{%raw%}{{ task.name }}{%endraw%}` |
| `property.name` | `{%raw%}{{ task.property.name }}{%endraw%}` |
| `ref` | `{%raw%}{{ task.ref }}{%endraw%}` |

</details>

<details class="expandable-section">
<summary><strong>Usage Examples</strong></summary>

```django
{% endblock %}
<p>Dear {{ attention }},</p>
<p>Please find attached our purchase order{% if task %} for {{ task.name }}{% endif %}.</p>
<p>Please deliver the parts to {{purchaseorder.delivery_instructions}} </p>
<p><strong>Delivery Address:<strong></p>
```

```django
{% for task in tasks %}
<p>
  Task {{ task.ref }}<br>
  {{ task.description }}<br>
  {{ task.property.name }}<br>
```

```django
<p>
  Task {{ task.ref }}<br>
  {{ task.description }}<br>
  {{ task.property.name }}<br>
  {{ task.address }}
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
| `status` | `{%raw%}{{ task_origin_defectquote.status }}{%endraw%}` |
| `status.upper` | `{%raw%}{{ task_origin_defectquote.status.upper }}{%endraw%}` |

</details>

<details class="expandable-section">
<summary><strong>Usage Examples</strong></summary>

```django
{% include "reports/library/arrow-up-right-from-square-icon.svg" with width="14" height="14" %}
          </a>
          <div class="status quote {{ task_origin_defectquote.status }} ml-2 mt-1">
            {{ task_origin_defectquote.status.upper }}
          </div>
```

```django
</a>
          <div class="status quote {{ task_origin_defectquote.status }} ml-2 mt-1">
            {{ task_origin_defectquote.status.upper }}
          </div>
        </div>
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
| `get_uuid_approval_url` | `{%raw%}{{ task_quote.get_uuid_approval_url\|absolute }}{%endraw%}` |
| `ref` | `{%raw%}{{ task_quote.ref }}{%endraw%}` |

</details>

<details class="expandable-section">
<summary><strong>Filters Used</strong></summary>

- `absolute`

</details>

<details class="expandable-section">
<summary><strong>Usage Examples</strong></summary>

```django
{% if task_quote.ref %}
        <div class="subtitle d-flex flex-row">
          <a href="{{ task_quote.get_uuid_approval_url|absolute }}">
            {{ task_quote.ref }}
            {% include "reports/library/arrow-up-right-from-square-icon.svg" with width="14" height="14" %}
```

```django
<div class="subtitle d-flex flex-row">
          <a href="{{ task_quote.get_uuid_approval_url|absolute }}">
            {{ task_quote.ref }}
            {% include "reports/library/arrow-up-right-from-square-icon.svg" with width="14" height="14" %}
          </a>
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
| `id` | `{%raw%}{{ tasksession.id }}{%endraw%}` |
| `technician.name` | `{%raw%}{{ tasksession.technician.name }}{%endraw%}` |

</details>

<details class="expandable-section">
<summary><strong>Usage Examples</strong></summary>

```django
</p>
<p>Thanks</p>
<p>Task Session {{ tasksession.id }} encountered an error while syncing to the accounting partner.</p>
{% if task %}
<p><b>Task:</b> {{ task }}</p>
```

```django
<p><b>Task:</b> {{ task }}</p>
{% endif %}
<p><b>Technician:</b> {{ tasksession.technician.name }}</p>
<p>Please review and address the error, then use the link below to retry the sync</p>
<p>
```

</details>

---

## template

<details class="expandable-section">
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details class="expandable-section">
<summary><strong>Usage Examples</strong></summary>

```django
<p>
  Change request: <a href="{{ base_url }}{{ changerequest.get_absolute_url }}">{{ changerequest.ref }}</a><br />
  Template: {% if template %}{{ template }}{% else %}New Template{% endif %}<br />
  Status: {{ changerequest.status }}
</p><p>Dear {{ client.name|default:'valued customer' }},</p>
```

</details>

---

## title

<details class="expandable-section">
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details class="expandable-section">
<summary><strong>Usage Examples</strong></summary>

```django
<div>
    <div class="uptick-heading d-flex flex-row justify-content-between w-100 no-page-break-after">
      <div>{{ title }}</div>
      {% if task_quote.ref %}
        <div class="subtitle d-flex flex-row">
```

</details>

---

## to_list

<details class="expandable-section">
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details class="expandable-section">
<summary><strong>Usage Examples</strong></summary>

```django
Email info:<br />
  Sent: {{ failure_datetime }}<br />
  To: {{ to_list }}<br />
  CC: {{ cc_list }}<br />
  Subject {{ subject }}<br />
```

</details>

---

## url

<details class="expandable-section">
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details class="expandable-section">
<summary><strong>Usage Examples</strong></summary>

```django
<p>A new message from {{ from }} is waiting for you:</p>
<p>{{ chat_message.text }}</p>
<p>{{ base_url }}{{ url }}</p>
<p>Regards, <br/>
{{ config.SITE_ORGANISATION }}
```

</details>

---


---
title: Django Template Variables Documentation
layout: default
---

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

<details>
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details>
<summary><strong>Usage Examples</strong></summary>

```django
{{ rectification.rejection_reason|markdowner }}
&lt;p&gt;Access the rectification to provide updated information:&lt;/p&gt;
&lt;p&gt;&lt;a href="{{ base_url }}{{ absolute_url }}"&gt;{{ base_url }}{{ absolute_url }}&lt;/a&gt;&lt;/p&gt;
{% endblock %}
{% extends 'email.html' %}
```

</details>

---

## approved_by

<details>
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details>
<summary><strong>Usage Examples</strong></summary>

```django
&lt;/p&gt;
&lt;p&gt;
The service quote for {{ property }} was approved by {{ approved_by }}.
&lt;/p&gt;
&lt;p&gt;
```

</details>

---

## appt

> This variable is typically used as a loop iterator

<details>
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details>
<summary><strong>Properties</strong></summary>

| Property | Examples |
|----------|----------|
| `scheduled_start` | {{appt.scheduled_start}} |
| `task.authorisation_ref` | {{appt.task.authorisation_ref}} |
| `task.description` | {{appt.task.description}} |
| `task.name` | {{appt.task.name}} |
| `task.property.name` | {{appt.task.property.name}} |
| `task.ref` | {{appt.task.ref}} |
| `task.scope_of_works` | {{appt.task.scope_of_works}} |
| `technicians.first` | {{appt.technicians.first}} |

</details>

<details>
<summary><strong>Usage Examples</strong></summary>

```django
{% timezone tmz %}
&lt;tr&gt;
&lt;th style="padding: 12px 10px; border-top: 1px solid #dcdddd;" scope="row" colspan="4"&gt;{{appt.scheduled_start}}&lt;/th&gt;
&lt;td style="padding: 12px 10px; border-top: 1px solid #dcdddd;"&gt;{{appt.task.description}}&lt;/td&gt;
&lt;td style="padding: 12px 10px; border-top: 1px solid #dcdddd;"&gt;{{appt.task.property.name}}&lt;/td&gt;
```

```django
&lt;tr&gt;
&lt;th style="padding: 12px 10px; border-top: 1px solid #dcdddd;" scope="row" colspan="4"&gt;{{appt.scheduled_start}}&lt;/th&gt;
&lt;td style="padding: 12px 10px; border-top: 1px solid #dcdddd;"&gt;{{appt.task.description}}&lt;/td&gt;
&lt;td style="padding: 12px 10px; border-top: 1px solid #dcdddd;"&gt;{{appt.task.property.name}}&lt;/td&gt;
&lt;td style="padding: 12px 10px; border-top: 1px solid #dcdddd;"&gt;{{appt.task.scope_of_works}}&lt;/td&gt;
```

```django
&lt;th style="padding: 12px 10px; border-top: 1px solid #dcdddd;" scope="row" colspan="4"&gt;{{appt.scheduled_start}}&lt;/th&gt;
&lt;td style="padding: 12px 10px; border-top: 1px solid #dcdddd;"&gt;{{appt.task.description}}&lt;/td&gt;
&lt;td style="padding: 12px 10px; border-top: 1px solid #dcdddd;"&gt;{{appt.task.property.name}}&lt;/td&gt;
&lt;td style="padding: 12px 10px; border-top: 1px solid #dcdddd;"&gt;{{appt.task.scope_of_works}}&lt;/td&gt;
&lt;td style="padding: 12px 10px; border-top: 1px solid #dcdddd;"&gt;{{appt.task.authorisation_ref}}&lt;/td&gt;
```

</details>

---

## attention

**Default values:** `Manager`, `manager`

<details>
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details>
<summary><strong>Filters Used</strong></summary>

- `default (arg: "Manager")`
- `default (arg: "manager")`

</details>

<details>
<summary><strong>Usage Examples</strong></summary>

```django
&lt;td style="width: 600px;"&gt;
&lt;div style="font-family: 'Arial', sans-serif; font-size: 10.5pt;"&gt;
&lt;p style="padding: 10px 0;"&gt;Dear {{ attention }},&lt;/p&gt;
&lt;p&gt;Please be advised we will need access to complete the following:&lt;/p&gt;
&lt;table style="width: 100%; border-collapse: collapse; border-bottom: 1px solid #dcdddd;"&gt;
```

```django
&lt;/table&gt;
{% endblock %}
&lt;p&gt;Dear {{ attention }},&lt;/p&gt;
&lt;p&gt;Please find attached your defect quote for {{ property.name }}.&lt;/p&gt;
&lt;p&gt;To view and approve this quote online, visit:&lt;/p&gt;
```

```django
&lt;p&gt;Regards,&lt;br /&gt;
{{ config.SITE_ORGANISATION }}&lt;/p&gt;
&lt;p&gt;Dear {{ attention|default:"manager" }},&lt;/p&gt;
&lt;p&gt;Please find attached your documents for services recently carried out at {{ property.name }}.&lt;/p&gt;
{% if invoice %}
```

</details>

---

## base_url

<details>
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details>
<summary><strong>Usage Examples</strong></summary>

```django
&lt;p&gt;Please find attached your defect quote for {{ property.name }}.&lt;/p&gt;
&lt;p&gt;To view and approve this quote online, visit:&lt;/p&gt;
&lt;p&gt;&lt;a href="{{ base_url }}{{ quote.get_uuid_approval_url }}"&gt;{{ base_url }}{{ quote.get_uuid_approval_url }}&lt;/a&gt;&lt;/p&gt;
&lt;p&gt;We value your opinion, please contact us with any comments you may have.&lt;/p&gt;
&lt;p&gt;Regards,&lt;br /&gt;
```

```django
&lt;ul&gt;
{% for quote in defectquotes %}
&lt;li&gt;Reference: {{ quote.ref }}&lt;a href="{{ base_url }}{{ quote.get_uuid_approval_url }}"&gt; (approve online)&lt;/a&gt;&lt;/li&gt;
{% endfor %}
&lt;/ul&gt;
```

```django
&lt;p&gt;
Please go to this URL to set your password and start using Uptick:
{{ base_url }}{% url 'password_reset_confirm' uidb64=uid token=token %}
&lt;/p&gt;
{% if account.license == "FIELD" %}
```

</details>

---

## bounce_address

<details>
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details>
<summary><strong>Usage Examples</strong></summary>

```django
&lt;p&gt;
Bounce info:&lt;br /&gt;
Address: {{ bounce_address }}&lt;br /&gt;
Bounce Reason: {{ formatted_reason }}&lt;br /&gt;
Email Subject {{ subject }}&lt;br /&gt;
```

</details>

---

## cc_list

<details>
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details>
<summary><strong>Usage Examples</strong></summary>

```django
Sent: {{ failure_datetime }}&lt;br /&gt;
To: {{ to_list }}&lt;br /&gt;
CC: {{ cc_list }}&lt;br /&gt;
Subject {{ subject }}&lt;br /&gt;
&lt;/p&gt;
```

</details>

---

## changerequest

<details>
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details>
<summary><strong>Properties</strong></summary>

| Property | Examples |
|----------|----------|
| `get_absolute_url` | {{ changerequest.get_absolute_url }} |
| `ref` | {{ changerequest.ref }} |
| `status` | {{ changerequest.status }} |

</details>

<details>
<summary><strong>Usage Examples</strong></summary>

```django
{{ config.SITE_ORGANISATION }}&lt;/p&gt;
{% if status == 'DRAFT' %}
&lt;p&gt;Template change request {{ changerequest.ref }} has been created for {{ customer }}.&lt;/p&gt;
{% elif  status == 'REQUESTED' %}
&lt;p&gt;{{ sender.name }} submitted feedback for Template change request {{ changerequest.ref }}.&lt;/p&gt;
```

```django
&lt;p&gt;Template change request {{ changerequest.ref }} has been created for {{ customer }}.&lt;/p&gt;
{% elif  status == 'REQUESTED' %}
&lt;p&gt;{{ sender.name }} submitted feedback for Template change request {{ changerequest.ref }}.&lt;/p&gt;
{% else %}
&lt;p&gt;Template change request {{ changerequest.ref }} has been approved. Our team will be in contact once completed.&lt;/p&gt;
```

```django
&lt;p&gt;{{ sender.name }} submitted feedback for Template change request {{ changerequest.ref }}.&lt;/p&gt;
{% else %}
&lt;p&gt;Template change request {{ changerequest.ref }} has been approved. Our team will be in contact once completed.&lt;/p&gt;
{% endif %}
&lt;p&gt;
```

</details>

---

## chat_message

<details>
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details>
<summary><strong>Properties</strong></summary>

| Property | Examples |
|----------|----------|
| `text` | {{ chat_message.text }} |

</details>

<details>
<summary><strong>Usage Examples</strong></summary>

```django
&lt;/p&gt;
&lt;p&gt;A new message from {{ from }} is waiting for you:&lt;/p&gt;
&lt;p&gt;{{ chat_message.text }}&lt;/p&gt;
&lt;p&gt;{{ base_url }}{{ url }}&lt;/p&gt;
&lt;p&gt;Regards, &lt;br/&gt;
```

```django
{% endblock %}
&lt;p&gt;A new message from {{ from }} is waiting for you:&lt;/p&gt;
&lt;p&gt;{{ chat_message.text }}&lt;/p&gt;
&lt;p&gt;{{ base_url }}{{ url }}&lt;/p&gt;
&lt;p&gt;Regards, &lt;br/&gt;
```

</details>

---

## client

<details>
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details>
<summary><strong>Properties</strong></summary>

| Property | Examples |
|----------|----------|
| `primary_contact.name` | {{ client.primary_contact.name }} |

</details>

<details>
<summary><strong>Usage Examples</strong></summary>

```django
&lt;p&gt;If the form{{ signoffproperties|pluralize }} on the attached link {{ signoffproperties|pluralize:"is,are" }} not submitted and there is no proof on site that the Essential Safety Measures are being serviced, {{ signoffproperties|pluralize:"a," }} Non-Compliant Building Report{{ signoffproperties|pluralize }} will be issued.&lt;/p&gt;
{% endblock %}
&lt;p&gt;Dear {{ client.primary_contact.name }},&lt;/p&gt;
&lt;p&gt;This email is in regards to your property {{ property.ref }} {{ property.name }} {{ property.client_ref }}.&lt;/p&gt;
&lt;p&gt;We have received notification from {{ contractor.name }} that they are no longer engaged to maintain the following items:&lt;/p&gt;
```

```django
&lt;div&gt;{{ servicequote.created|date:"jS F Y" }}&lt;/div&gt;
{% if servicequote.expiry_date %}&lt;div&gt;This quote is valid until &lt;em&gt;{{ servicequote.expiry_date }}&lt;/em&gt;&lt;/div&gt;{% endif %}
&lt;div&gt;&lt;strong&gt;Attention: {{ client.primary_contact.name }}&lt;/strong&gt;&lt;/div&gt;
{% if servicequote.scope_of_works %}
&lt;div class="mt-3"&gt;
```

</details>

---

## config

<details>
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details>
<summary><strong>Properties</strong></summary>

| Property | Examples |
|----------|----------|
| `CONTACT_EMAIL` | {{ config.CONTACT_EMAIL }} |
| `CONTACT_PHONE` | {{config.CONTACT_PHONE}} |
| `SITE_ORGANISATION` | {{config.SITE_ORGANISATION}} |

</details>

<details>
<summary><strong>Usage Examples</strong></summary>

```django
&lt;p&gt;{{request_user.email}}&lt;/p&gt;
&lt;p&gt;
{{ config.CONTACT_PHONE }} &lt;br /&gt;
{{ config.SITE_ORGANISATION }}
&lt;/p&gt;
```

```django
&lt;p&gt;
{{ config.CONTACT_PHONE }} &lt;br /&gt;
{{ config.SITE_ORGANISATION }}
&lt;/p&gt;
&lt;/div&gt;
```

```django
&lt;p&gt;We value your opinion, please contact us with any comments you may have.&lt;/p&gt;
&lt;p&gt;Regards,&lt;br /&gt;
{{ config.SITE_ORGANISATION }}&lt;/p&gt;
&lt;p&gt;Dear {{ attention|default:"manager" }},&lt;/p&gt;
&lt;p&gt;Please find attached your documents for services recently carried out at {{ property.name }}.&lt;/p&gt;
```

</details>

---

## contractor

<details>
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details>
<summary><strong>Properties</strong></summary>

| Property | Examples |
|----------|----------|
| `account` | {{ contractor.account }} |
| `name` | {{ contractor.name }} |

</details>

<details>
<summary><strong>Usage Examples</strong></summary>

```django
{{ config.SITE_ORGANISATION }}&lt;/p&gt;
{% endblock %}
&lt;p&gt;Dear {{ contractor }},&lt;/p&gt;
&lt;p&gt;You have been assigned the following tasks:&lt;/p&gt;
{% for task in tasks %}
```

```django
&lt;p&gt;You can provide your field technicians with this link which will enable them to complete the task via their smart phone (apple or android) without needing to install an app.&lt;/p&gt;
&lt;p&gt;Thanks&lt;/p&gt;
&lt;p&gt;The contractor {{ contractor }} has rejected the task assigned to him for the following reason: {{ rejection_reason }}&lt;/p&gt;
&lt;p&gt;
The task that was assigned was:&lt;br&gt;
```

```django
&lt;/p&gt;
&lt;p&gt;Thanks&lt;/p&gt;
&lt;p&gt;Dear {{ contractor }},&lt;/p&gt;
&lt;p&gt;Please be advised that the following task has been cancelled:&lt;/p&gt;
&lt;ul&gt;
```

</details>

---

## contractor_contact

<details>
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details>
<summary><strong>Properties</strong></summary>

| Property | Examples |
|----------|----------|
| `name` | {{ contractor_contact.name }} |

</details>

<details>
<summary><strong>Usage Examples</strong></summary>

```django
&lt;p&gt;Regards,&lt;br/&gt;
{{ config.SITE_ORGANISATION }}&lt;/p&gt;
&lt;p&gt;Dear {{ contractor_contact }},&lt;/p&gt;
&lt;p&gt;Please be advised that the following task has been cancelled:&lt;/p&gt;
&lt;ul&gt;
```

```django
{{ config.SITE_ORGANISATION }}
&lt;/p&gt;
&lt;p&gt;Dear {{ contractor_contact.name }},&lt;/p&gt;
&lt;p&gt;You have been assigned a task:&lt;/p&gt;
&lt;p&gt;Task {{ task.ref }}&lt;/p&gt;
```

```django
&lt;/p&gt;
&lt;p&gt;Thanks&lt;/p&gt;
&lt;p&gt;Dear {{ contractor_contact.name }},&lt;/p&gt;
&lt;p&gt;You have been assigned the following tasks:&lt;/p&gt;
{% for task in tasks %}
```

</details>

---

## contractor_login_url

<details>
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details>
<summary><strong>Usage Examples</strong></summary>

```django
&lt;p&gt;
Please sign in the contractor portal using the link below to view a list of any outstanding tasks:&lt;br&gt;
&lt;a href="{{ contractor_login_url }}"&gt;{{ contractor_login_url }}&lt;/a&gt;
&lt;/p&gt;
&lt;p&gt;You can provide your field technicians with this link which will enable them to complete the task via their smart phone (apple or android) without needing to install an app.&lt;/p&gt;
```

```django
&lt;p&gt;
Please visit the task dashboard on Uptick:&lt;br&gt;
&lt;a href="{{ contractor_login_url }}"&gt;{{ contractor_login_url }}&lt;/a&gt;&lt;br&gt;
for more details.
&lt;/p&gt;
```

```django
&lt;p&gt;{{ task.address }}&lt;/p&gt;
&lt;p&gt;Please sign into the contractor portal using the link below to view your outstanding tasks:&lt;br&gt;
&lt;a href="{{ contractor_login_url }}"&gt;{{ contractor_login_url }}&lt;/a&gt;
&lt;/p&gt;
&lt;p&gt;Thanks&lt;/p&gt;
```

</details>

---

## csv_url

<details>
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details>
<summary><strong>Usage Examples</strong></summary>

```django
&lt;p&gt;Your custom report, {{ name }}, has been generated.&lt;/p&gt;
&lt;p&gt;{{ description }}&lt;/p&gt;
&lt;p&gt;To download, &lt;a href="{{ csv_url }}"&gt;please click here&lt;/a&gt;.&lt;/p&gt;
{% endblock %}
&lt;p&gt;Dear {{ attention }},&lt;/p&gt;
```

</details>

---

## custom_message

<details>
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details>
<summary><strong>Usage Examples</strong></summary>

```django
{% if custom_message %}
&lt;p&gt;
{{ custom_message }}
&lt;/p&gt;
{% endif %}
```

</details>

---

## customer

<details>
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details>
<summary><strong>Usage Examples</strong></summary>

```django
{{ config.SITE_ORGANISATION }}&lt;/p&gt;
{% if status == 'DRAFT' %}
&lt;p&gt;Template change request {{ changerequest.ref }} has been created for {{ customer }}.&lt;/p&gt;
{% elif  status == 'REQUESTED' %}
&lt;p&gt;{{ sender.name }} submitted feedback for Template change request {{ changerequest.ref }}.&lt;/p&gt;
```

</details>

---

## declined_by

<details>
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details>
<summary><strong>Usage Examples</strong></summary>

```django
&lt;/p&gt;
&lt;p&gt;
The service quote for {{ property }} was declined by {{ declined_by }}.
&lt;/p&gt;
&lt;p&gt;
```

</details>

---

## description

<details>
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details>
<summary><strong>Usage Examples</strong></summary>

```django
{% block content %}
&lt;p&gt;Your custom report, {{ name }}, has been generated.&lt;/p&gt;
&lt;p&gt;{{ description }}&lt;/p&gt;
&lt;p&gt;To download, &lt;a href="{{ csv_url }}"&gt;please click here&lt;/a&gt;.&lt;/p&gt;
{% endblock %}
```

</details>

---

## email

> This variable is typically used as a loop iterator

<details>
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details>
<summary><strong>Usage Examples</strong></summary>

```django
{% for email in quote_email_lookup|getvalue:quote %}
{% if email != recipient %}
&lt;li&gt;{{email}}&lt;/li&gt;
{% endif %}
{% endfor %}
```

</details>

---

## end_date

<details>
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details>
<summary><strong>Usage Examples</strong></summary>

```django
&lt;td style="border: 3px double #000; padding: 8px; width: 25%;"&gt;{{start_date}}&lt;/td&gt;
&lt;td style="border: 3px double #000; padding: 8px; width: 25%; background-color: #f0f0f0;"&gt;END DATE&lt;/td&gt;
&lt;td style="border: 3px double #000; padding: 8px; width: 25%;"&gt;{{end_date}}&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
```

</details>

---

## exception

<details>
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details>
<summary><strong>Usage Examples</strong></summary>

```django
&lt;/p&gt;
&lt;h3&gt;Error&lt;/h3&gt;
&lt;code&gt;{{ exception }}&lt;/code&gt;
&lt;p&gt;
An email failed to send from Uptick! This is sometimes due to an invalid email, but more details below.
```

</details>

---

## failure_datetime

<details>
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details>
<summary><strong>Usage Examples</strong></summary>

```django
&lt;p&gt;
Email info:&lt;br /&gt;
Sent: {{ failure_datetime }}&lt;br /&gt;
To: {{ to_list }}&lt;br /&gt;
CC: {{ cc_list }}&lt;br /&gt;
```

</details>

---

## failure_reason

<details>
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details>
<summary><strong>Usage Examples</strong></summary>

```django
An email failed to send from Uptick! This is sometimes due to an invalid email, but more details below.
&lt;br /&gt;
{{ failure_reason }}
&lt;/p&gt;
&lt;p&gt;
```

</details>

---

## formatted_reason

<details>
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details>
<summary><strong>Usage Examples</strong></summary>

```django
Bounce info:&lt;br /&gt;
Address: {{ bounce_address }}&lt;br /&gt;
Bounce Reason: {{ formatted_reason }}&lt;br /&gt;
Email Subject {{ subject }}&lt;br /&gt;
Email Sent: {{ formatted_timestamp }}
```

</details>

---

## formatted_timestamp

<details>
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details>
<summary><strong>Usage Examples</strong></summary>

```django
Bounce Reason: {{ formatted_reason }}&lt;br /&gt;
Email Subject {{ subject }}&lt;br /&gt;
Email Sent: {{ formatted_timestamp }}
&lt;/p&gt;
&lt;p&gt;
```

</details>

---

## formresponse

> This variable is typically used as a loop iterator

<details>
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details>
<summary><strong>Properties</strong></summary>

| Property | Examples |
|----------|----------|
| `submitter` | {{ formresponse.submitter }} |
| `template_version.template.name` | {{ formresponse.template_version.template.name }} |

</details>

<details>
<summary><strong>Usage Examples</strong></summary>

```django
&lt;ul&gt;
{% for formresponse in formresponses %}
&lt;li&gt;{{ formresponse }}&lt;/li&gt;
{% endfor %}
&lt;/ul&gt;
```

```django
&lt;/p&gt;&lt;p&gt;Dear {{ attention }},&lt;/p&gt;
&lt;p&gt;Please find attached a form response regarding work at {{ property.name }}.&lt;/p&gt;
&lt;p&gt;Form: {{ formresponse.template_version.template.name }}&lt;/p&gt;
&lt;p&gt;Submitted by: {{ formresponse.submitter }}&lt;/p&gt;
&lt;p&gt;We value your opinion, please contact us with any comments you may have.&lt;/p&gt;
```

```django
&lt;p&gt;Please find attached a form response regarding work at {{ property.name }}.&lt;/p&gt;
&lt;p&gt;Form: {{ formresponse.template_version.template.name }}&lt;/p&gt;
&lt;p&gt;Submitted by: {{ formresponse.submitter }}&lt;/p&gt;
&lt;p&gt;We value your opinion, please contact us with any comments you may have.&lt;/p&gt;
&lt;p&gt;Regards,&lt;br /&gt;
```

</details>

---

## from

<details>
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details>
<summary><strong>Usage Examples</strong></summary>

```django
{{ config.SITE_ORGANISATION }}
&lt;/p&gt;
&lt;p&gt;A new message from {{ from }} is waiting for you:&lt;/p&gt;
&lt;p&gt;{{ chat_message.text }}&lt;/p&gt;
&lt;p&gt;{{ base_url }}{{ url }}&lt;/p&gt;
```

```django
{% endfor %}
{% endblock %}
&lt;p&gt;A new message from {{ from }} is waiting for you:&lt;/p&gt;
&lt;p&gt;{{ chat_message.text }}&lt;/p&gt;
&lt;p&gt;{{ base_url }}{{ url }}&lt;/p&gt;
```

</details>

---

## inv

> This variable is typically used as a loop iterator

<details>
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details>
<summary><strong>Properties</strong></summary>

| Property | Examples |
|----------|----------|
| `number` | {{ inv.number }} |
| `ref` | {{ inv.ref }} |

</details>

<details>
<summary><strong>Usage Examples</strong></summary>

```django
&lt;p&gt;This is a reminder that we are waiting for your payment on the following invoices:&lt;br&gt;
{% for inv in invoices %}&lt;br&gt;
Number: {{ inv.number }}&lt;br&gt;
Reference: {{ inv.ref }}&lt;br&gt;
Due: {{ inv.due_date|date:"jS F Y" }}&lt;br&gt;
```

```django
{% for inv in invoices %}&lt;br&gt;
Number: {{ inv.number }}&lt;br&gt;
Reference: {{ inv.ref }}&lt;br&gt;
Due: {{ inv.due_date|date:"jS F Y" }}&lt;br&gt;
{% endfor %}
```

</details>

---

## invoice

<details>
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details>
<summary><strong>Properties</strong></summary>

| Property | Examples |
|----------|----------|
| `ref` | {{ invoice.ref }} |

</details>

<details>
<summary><strong>Usage Examples</strong></summary>

```django
&lt;p&gt;Your invoice:&lt;/p&gt;
&lt;ul&gt;
&lt;li&gt;{{ invoice.number|default:"[[ invoice_number ]]" }} {% if invoice.ref %}({{ invoice.ref }}){% endif %}&lt;/li&gt;
&lt;/ul&gt;
{% endif %}
```

</details>

---

## item

> This variable is typically used as a loop iterator

<details>
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details>
<summary><strong>Properties</strong></summary>

| Property | Examples |
|----------|----------|
| `label` | {{ item.label }} |

</details>

<details>
<summary><strong>Usage Examples</strong></summary>

```django
&lt;ul&gt;
{% for item in items %}
&lt;li&gt;{{ item.label }}&lt;/li&gt;
{% endfor %}
&lt;/ul&gt;
```

</details>

---

## lead_engineer

<details>
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details>
<summary><strong>Usage Examples</strong></summary>

```django
&lt;tr&gt;
&lt;td style="border: 3px double #000; padding: 8px; background-color: #f0f0f0;"&gt;LEAD ENGINEER&lt;/td&gt;
&lt;td style="border: 3px double #000; padding: 8px;" colspan="3"&gt;{{lead_engineer}}&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
```

</details>

---

## line

> This variable is typically used as a loop iterator

<details>
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details>
<summary><strong>Properties</strong></summary>

| Property | Examples |
|----------|----------|
| `annual_subtotal` | {{ line.annual_subtotal|currency }} |
| `product.name` | {{ line.product.name }} |
| `quantity` | {{ line.quantity|floatformat:2 }} |
| `routineservicetype.name` | {{ line.routineservicetype.name }} |
| `site_price` | {{ line.site_price|currency }} |
| `subtotal` | {{ line.subtotal|currency }} |
| `unit_price` | {{ line.unit_price|currency }} |

</details>

<details>
<summary><strong>Filters Used</strong></summary>

- `currency`
- `floatformat (arg: 2)`

</details>

<details>
<summary><strong>Usage Examples</strong></summary>

```django
&lt;tr class="keep-together"&gt;
&lt;td&gt;
&lt;div&gt;{{ line.product.name }}&lt;/div&gt;
&lt;div class="text-muted"&gt;{{ line.description|default:'-' }}&lt;/div&gt;
&lt;/td&gt;
```

```django
&lt;div class="text-muted"&gt;{{ line.description|default:'-' }}&lt;/div&gt;
&lt;/td&gt;
&lt;td class="text-right"&gt;{{ line.quantity|floatformat:2 }}&lt;/td&gt;
&lt;td class="text-right"&gt;{{ line.unit_price|currency }}&lt;/td&gt;
&lt;td class="text-right"&gt;{{ line.subtotal|currency }}&lt;/td&gt;
```

```django
&lt;/td&gt;
&lt;td class="text-right"&gt;{{ line.quantity|floatformat:2 }}&lt;/td&gt;
&lt;td class="text-right"&gt;{{ line.unit_price|currency }}&lt;/td&gt;
&lt;td class="text-right"&gt;{{ line.subtotal|currency }}&lt;/td&gt;
&lt;/tr&gt;
```

</details>

---

## logbook

> This variable is typically used as a loop iterator

<details>
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details>
<summary><strong>Properties</strong></summary>

| Property | Examples |
|----------|----------|
| `name` | {{ logbook.name }} |

</details>

<details>
<summary><strong>Usage Examples</strong></summary>

```django
&lt;ul&gt;
{% for logbook in digital_logbooks %}
&lt;li&gt;{{ logbook.name }}&lt;/li&gt;
{% endfor %}
&lt;/ul&gt;
```

</details>

---

## login_url

<details>
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details>
<summary><strong>Usage Examples</strong></summary>

```django
&lt;tr&gt;
&lt;td align="center" bgcolor="#27a9e3"&gt;
&lt;a style="color: white; text-decoration: underline;" href="{{ login_url }}"&gt;
Open your contractor portal
&lt;/a&gt;
```

</details>

---

## message

<details>
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details>
<summary><strong>Usage Examples</strong></summary>

```django
{% endblock %}
&lt;p&gt;A webhook event from Corrigo was rejected.&lt;/p&gt;
&lt;p&gt;Reason: {{ message }}&lt;/p&gt;
&lt;p&gt;Payload:&lt;p&gt;
&lt;pre&gt;&lt;code&gt;{{payload}}&lt;/code&gt;&lt;/pre&gt;
```

```django
{{ property_refs|join:", " }}
&lt;br /&gt;
{{ message }}
&lt;/li&gt;
&lt;/ul&gt;
```

</details>

---

## name

<details>
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details>
<summary><strong>Usage Examples</strong></summary>

```django
\{% extends 'email.html' %}
{% block content %}
&lt;p&gt;Your custom report, {{ name }}, has been generated.&lt;/p&gt;
&lt;p&gt;{{ description }}&lt;/p&gt;
&lt;p&gt;To download, &lt;a href="{{ csv_url }}"&gt;please click here&lt;/a&gt;.&lt;/p&gt;
```

</details>

---

## no_of_assets

<details>
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details>
<summary><strong>Usage Examples</strong></summary>

```django
&lt;p&gt;Regards,&lt;br /&gt;
Uptick Team&lt;/p&gt;
&lt;p&gt;There are currently {{ no_of_assets }} assets not covered by any Routines. These assets relate to the following properties:&lt;/p&gt;
&lt;ul&gt;
{% for property in properties %}
```

</details>

---

## payload

<details>
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details>
<summary><strong>Usage Examples</strong></summary>

```django
&lt;p&gt;Reason: {{ message }}&lt;/p&gt;
&lt;p&gt;Payload:&lt;p&gt;
&lt;pre&gt;&lt;code&gt;{{payload}}&lt;/code&gt;&lt;/pre&gt;
&lt;p&gt;Regards,&lt;br /&gt;
Uptick Team&lt;/p&gt;
```

</details>

---

## promptset

<details>
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details>
<summary><strong>Properties</strong></summary>

| Property | Examples |
|----------|----------|
| `name` | {{ promptset.name }} |
| `ref` | {{ promptset.ref }} |

</details>

<details>
<summary><strong>Usage Examples</strong></summary>

```django
&lt;tr&gt;
&lt;th colspan="3" class="border-top-0"&gt;
({{ promptset.ref }}) {{ promptset.name }}
&lt;/th&gt;
&lt;/tr&gt;
```

</details>

---

## property

> This variable is typically used as a loop iterator

<details>
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details>
<summary><strong>Properties</strong></summary>

| Property | Examples |
|----------|----------|
| `client_ref` | {{ property.client_ref }} |
| `name` | {{ property.name }} |
| `property__name` | {{ property.property__name }} |
| `property_id` | {{property.property_id}} |
| `ref` | {{ property.ref }} |

</details>

<details>
<summary><strong>Usage Examples</strong></summary>

```django
{% endblock %}
&lt;p&gt;Dear {{ attention }},&lt;/p&gt;
&lt;p&gt;Please find attached your defect quote for {{ property.name }}.&lt;/p&gt;
&lt;p&gt;To view and approve this quote online, visit:&lt;/p&gt;
&lt;p&gt;&lt;a href="{{ base_url }}{{ quote.get_uuid_approval_url }}"&gt;{{ base_url }}{{ quote.get_uuid_approval_url }}&lt;/a&gt;&lt;/p&gt;
```

```django
{{ config.SITE_ORGANISATION }}&lt;/p&gt;
&lt;p&gt;Dear {{ attention|default:"manager" }},&lt;/p&gt;
&lt;p&gt;Please find attached your documents for services recently carried out at {{ property.name }}.&lt;/p&gt;
{% if invoice %}
&lt;p&gt;Your invoice:&lt;/p&gt;
```

```django
&lt;p&gt;For any questions, please contact us.&lt;/p&gt;
&lt;p&gt;Dear {{ attention|default:"manager" }},&lt;/p&gt;
&lt;p&gt;Please find attached your documents for services recently carried out at {{ property.name }}.&lt;/p&gt;
{% if invoice %}
&lt;p&gt;Your invoice:&lt;/p&gt;
```

</details>

---

## purchaseorder

<details>
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details>
<summary><strong>Properties</strong></summary>

| Property | Examples |
|----------|----------|
| `delivery_instructions` | {{purchaseorder.delivery_instructions}} |

</details>

<details>
<summary><strong>Usage Examples</strong></summary>

```django
&lt;p&gt;Dear {{ attention }},&lt;/p&gt;
&lt;p&gt;Please find attached our purchase order{% if task %} for {{ task.name }}{% endif %}.&lt;/p&gt;
&lt;p&gt;Please deliver the parts to {{purchaseorder.delivery_instructions}} &lt;/p&gt;
&lt;p&gt;&lt;strong&gt;Delivery Address:&lt;strong&gt;&lt;/p&gt;
&lt;p&gt;Regards,&lt;br /&gt;
```

</details>

---

## quote

> This variable is typically used as a loop iterator

<details>
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details>
<summary><strong>Properties</strong></summary>

| Property | Examples |
|----------|----------|
| `get_uuid_approval_url` | {{ quote.get_uuid_approval_url }} |
| `property.name` | {{ quote.property.name }} |
| `ref` | {{ quote.ref }} |
| `status.upper` | {{ quote.status.upper }} |

</details>

<details>
<summary><strong>Filters Used</strong></summary>

- `absolute`

</details>

<details>
<summary><strong>Usage Examples</strong></summary>

```django
&lt;p&gt;Please find attached your defect quote for {{ property.name }}.&lt;/p&gt;
&lt;p&gt;To view and approve this quote online, visit:&lt;/p&gt;
&lt;p&gt;&lt;a href="{{ base_url }}{{ quote.get_uuid_approval_url }}"&gt;{{ base_url }}{{ quote.get_uuid_approval_url }}&lt;/a&gt;&lt;/p&gt;
&lt;p&gt;We value your opinion, please contact us with any comments you may have.&lt;/p&gt;
&lt;p&gt;Regards,&lt;br /&gt;
```

```django
&lt;ul&gt;
{% for quote in defectquotes %}
&lt;li&gt;Reference: {{ quote.ref }}&lt;a href="{{ base_url }}{{ quote.get_uuid_approval_url }}"&gt; (approve online)&lt;/a&gt;&lt;/li&gt;
{% endfor %}
&lt;/ul&gt;
```

```django
{% endif %}
&lt;p&gt;To view and approve this quote online, visit:&lt;/p&gt;
&lt;p&gt;&lt;a href="{{ base_url }}{{ quote.get_uuid_approval_url }}"&gt;{{ base_url }}{{ quote.get_uuid_approval_url }}&lt;/a&gt;&lt;/p&gt;
&lt;p&gt;Regards,&lt;br /&gt;
{{ config.SITE_ORGANISATION }}&lt;/p&gt;
```

</details>

---

## rectification

<details>
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details>
<summary><strong>Properties</strong></summary>

| Property | Examples |
|----------|----------|
| `ref` | {{ rectification.ref }} |
| `rejection_reason` | {{ rectification.rejection_reason|markdowner }} |

</details>

<details>
<summary><strong>Filters Used</strong></summary>

- `markdowner`

</details>

<details>
<summary><strong>Usage Examples</strong></summary>

```django
{% load markdowner %}
{% block content %}
&lt;h4&gt;Rectification {{ rectification.ref }} was rejected.&lt;/h4&gt;
&lt;p&gt;Reason provided:&lt;/p&gt;
{{ rectification.rejection_reason|markdowner }}
```

```django
&lt;h4&gt;Rectification {{ rectification.ref }} was rejected.&lt;/h4&gt;
&lt;p&gt;Reason provided:&lt;/p&gt;
{{ rectification.rejection_reason|markdowner }}
&lt;p&gt;Access the rectification to provide updated information:&lt;/p&gt;
&lt;p&gt;&lt;a href="{{ base_url }}{{ absolute_url }}"&gt;{{ base_url }}{{ absolute_url }}&lt;/a&gt;&lt;/p&gt;
```

</details>

---

## ref_no

<details>
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details>
<summary><strong>Usage Examples</strong></summary>

```django
&lt;tr&gt;
&lt;td style="border: 3px double #000; padding: 8px; background-color: #f0f0f0;"&gt;OUR REF NO.&lt;/td&gt;
&lt;td style="border: 3px double #000; padding: 8px;" colspan="3"&gt;{{ref_no}}&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
```

```django
&lt;tr&gt;
&lt;td style="border: 3px double #000; padding: 8px; background-color: #f0f0f0;"&gt;VISIT No.&lt;/td&gt;
&lt;td style="border: 3px double #000; padding: 8px;" colspan="3"&gt;{{ref_no}}&lt;/td&gt;
&lt;/tr&gt;
&lt;tr&gt;
```

</details>

---

## rejection_reason

<details>
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details>
<summary><strong>Usage Examples</strong></summary>

```django
&lt;p&gt;You can provide your field technicians with this link which will enable them to complete the task via their smart phone (apple or android) without needing to install an app.&lt;/p&gt;
&lt;p&gt;Thanks&lt;/p&gt;
&lt;p&gt;The contractor {{ contractor }} has rejected the task assigned to him for the following reason: {{ rejection_reason }}&lt;/p&gt;
&lt;p&gt;
The task that was assigned was:&lt;br&gt;
```

</details>

---

## remark

> This variable is typically used as a loop iterator

<details>
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details>
<summary><strong>Properties</strong></summary>

| Property | Examples |
|----------|----------|
| `get_description` | {{ remark.get_description|markdowner }} |
| `get_public_url` | {{ remark.get_public_url }} |
| `get_resolution` | {{ remark.get_resolution|markdowner }} |
| `get_severity_display` | {{ remark.get_severity_display }} |
| `id` | {{ remark.id }} |
| `identified` | {{ remark.identified }} |
| `last_verified_date` | {{ remark.last_verified_date }} |
| `location` | {{ remark.location|markdowner }} |
| `severity` | {{ remark.severity }} |

</details>

<details>
<summary><strong>Filters Used</strong></summary>

- `markdowner`

</details>

<details>
<summary><strong>Usage Examples</strong></summary>

```django
&lt;tr&gt;
&lt;td class="m-0 p-0"&gt;
&lt;div id="{{ remark.id }}"
class="remark severity-{{ remark.severity }} keep-together"&gt;
&lt;div class="d-flex flex-row justify-content-between header"&gt;
```

```django
&lt;td class="m-0 p-0"&gt;
&lt;div id="{{ remark.id }}"
class="remark severity-{{ remark.severity }} keep-together"&gt;
&lt;div class="d-flex flex-row justify-content-between header"&gt;
&lt;div class="px-3 py-2"&gt;
```

```django
&lt;div class="d-flex flex-row justify-content-between header"&gt;
&lt;div class="px-3 py-2"&gt;
&lt;strong&gt;{{ remark.get_severity_display }}&lt;/strong&gt;
&lt;br/&gt;
&lt;a href="{{ remark.get_public_url }}"&gt;
```

</details>

---

## report

> This variable is typically used as a loop iterator

<details>
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details>
<summary><strong>Properties</strong></summary>

| Property | Examples |
|----------|----------|
| `get_title` | {{ report.get_title }} |

</details>

<details>
<summary><strong>Usage Examples</strong></summary>

```django
&lt;ul&gt;
{% for report in reports %}
&lt;li&gt;{{ report.get_title }} ({{ report.compliant|yesno:"compliant,non-compliant,not applicable"}})&lt;/li&gt;
{% endfor %}
&lt;/ul&gt;
```

</details>

---

## request_user

<details>
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details>
<summary><strong>Properties</strong></summary>

| Property | Examples |
|----------|----------|
| `email` | {{request_user.email}} |
| `name` | {{request_user.name}} |

</details>

<details>
<summary><strong>Usage Examples</strong></summary>

```django
&lt;/tbody&gt;
&lt;/table&gt;
&lt;p&gt;If you have any queries or need to change the time, please email me at &lt;a href="mailto:{{request_user.email}}"&gt;{{request_user.email}}&lt;/a&gt;.&lt;/p&gt;
&lt;p&gt;Regards,&lt;br&gt;
{{request_user.name}}&lt;/p&gt;
```

```django
&lt;p&gt;If you have any queries or need to change the time, please email me at &lt;a href="mailto:{{request_user.email}}"&gt;{{request_user.email}}&lt;/a&gt;.&lt;/p&gt;
&lt;p&gt;Regards,&lt;br&gt;
{{request_user.name}}&lt;/p&gt;
&lt;p&gt;{{request_user.email}}&lt;/p&gt;
&lt;p&gt;
```

```django
&lt;p&gt;Regards,&lt;br&gt;
{{request_user.name}}&lt;/p&gt;
&lt;p&gt;{{request_user.email}}&lt;/p&gt;
&lt;p&gt;
{{ config.CONTACT_PHONE }} &lt;br /&gt;
```

</details>

---

## retry_link

<details>
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details>
<summary><strong>Usage Examples</strong></summary>

```django
&lt;p&gt;Please review and address the error, then use the link below to retry the sync&lt;/p&gt;
&lt;p&gt;
&lt;a href={{ retry_link }}&gt;Click here&lt;/a&gt; and use the &lt;code&gt;POST&lt;/code&gt; button to retry the sync.
&lt;/p&gt;
&lt;h3&gt;Error&lt;/h3&gt;
```

</details>

---

## routineserviceleveltype

<details>
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details>
<summary><strong>Properties</strong></summary>

| Property | Examples |
|----------|----------|
| `get_routine_display_name` | {{ routineserviceleveltype.get_routine_display_name }} |
| `routineservicetype.standard.name` | {{ routineserviceleveltype.routineservicetype.standard.name }} |

</details>

<details>
<summary><strong>Usage Examples</strong></summary>

```django
{% for routineserviceleveltype, servicetask_group in servicetasks_grouped_by_type %}
&lt;div class="uptick-title no-page-break-after"&gt;
&lt;div&gt;{{ routineserviceleveltype.get_routine_display_name }}&lt;/div&gt;
{% if routineserviceleveltype.routineservicetype.standard.name != "Default" %}
&lt;div className="text-muted"&gt;&lt;small&gt;{{ routineserviceleveltype.routineservicetype.standard.name }}&lt;/small&gt;&lt;/div&gt;
```

```django
&lt;div&gt;{{ routineserviceleveltype.get_routine_display_name }}&lt;/div&gt;
{% if routineserviceleveltype.routineservicetype.standard.name != "Default" %}
&lt;div className="text-muted"&gt;&lt;small&gt;{{ routineserviceleveltype.routineservicetype.standard.name }}&lt;/small&gt;&lt;/div&gt;
{% endif %}
&lt;/div&gt;
```

</details>

---

## rslt

> This variable is typically used as a loop iterator

<details>
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details>
<summary><strong>Properties</strong></summary>

| Property | Examples |
|----------|----------|
| `name` | {{ rslt.name }} |

</details>

<details>
<summary><strong>Usage Examples</strong></summary>

```django
{{ line.routineservicetype.name }} –
{% for rslt in line.routineserviceleveltypes.all %}
&lt;span&gt;{{ rslt.name }}{% if not forloop.last %}, {% endif %}&lt;/span&gt;
{% endfor %}
&lt;/div&gt;
```

```django
&lt;div&gt;{{ line.routineservicetype.name }}&lt;/div&gt;
{% for rslt in line.routineserviceleveltypes.all %}
&lt;span&gt;{{ rslt.name }}{% if not forloop.last %},{% endif %}&lt;/span&gt;
{% endfor %}
&lt;/div&gt;
```

</details>

---

## scope_of_works

<details>
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details>
<summary><strong>Usage Examples</strong></summary>

```django
&lt;tr&gt;
&lt;td style="border: 3px double #000; padding: 8px; background-color: #f0f0f0;"&gt;SCOPE OF WORKS&lt;/td&gt;
&lt;td style="border: 3px double #000; padding: 8px;" colspan="3"&gt;{{scope_of_works}}&lt;/td&gt;
&lt;/tr&gt;
&lt;/table&gt;
```

</details>

---

## sender

<details>
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details>
<summary><strong>Properties</strong></summary>

| Property | Examples |
|----------|----------|
| `name` | {{ sender.name }} |

</details>

<details>
<summary><strong>Usage Examples</strong></summary>

```django
&lt;p&gt;Template change request {{ changerequest.ref }} has been created for {{ customer }}.&lt;/p&gt;
{% elif  status == 'REQUESTED' %}
&lt;p&gt;{{ sender.name }} submitted feedback for Template change request {{ changerequest.ref }}.&lt;/p&gt;
{% else %}
&lt;p&gt;Template change request {{ changerequest.ref }} has been approved. Our team will be in contact once completed.&lt;/p&gt;
```

</details>

---

## servicequote

<details>
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details>
<summary><strong>Properties</strong></summary>

| Property | Examples |
|----------|----------|
| `annual_gst` | {{ servicequote.annual_gst|currency }} |
| `annual_subtotal` | {{ servicequote.annual_subtotal|currency }} |
| `annual_total` | {{ servicequote.annual_total|currency }} |
| `description` | {{ servicequote.description }} |
| `expiry_date` | {{ servicequote.expiry_date }} |
| `get_absolute_url` | {{ servicequote.get_absolute_url }} |
| `product_gst` | {{ servicequote.product_gst|currency }} |
| `product_subtotal` | {{ servicequote.product_subtotal|currency }} |
| `product_total` | {{ servicequote.product_total|currency }} |
| `ref` | {{ servicequote.ref }} |
| `salesperson.email` | {{ servicequote.salesperson.email }} |
| `salesperson.name` | {{ servicequote.salesperson.name }} |
| `scope_of_works` | {{ servicequote.scope_of_works|markdowner }} |
| `terms_and_conditions` | {{ servicequote.terms_and_conditions|markdowner }} |

</details>

<details>
<summary><strong>Filters Used</strong></summary>

- `currency`
- `markdowner`

</details>

<details>
<summary><strong>Usage Examples</strong></summary>

```django
&lt;div&gt;
&lt;strong&gt;Scope of works:&lt;/strong&gt;
{{ servicequote.description }}
&lt;/div&gt;
&lt;br /&gt;
```

```django
Kind regards,&lt;br /&gt;&lt;br /&gt;
{% if servicequote.salesperson %}
&lt;div&gt;{{ servicequote.salesperson.name }}&lt;/div&gt;
&lt;div&gt;{{ servicequote.salesperson.email }}&lt;/div&gt;
{% endif %}
```

```django
{% if servicequote.salesperson %}
&lt;div&gt;{{ servicequote.salesperson.name }}&lt;/div&gt;
&lt;div&gt;{{ servicequote.salesperson.email }}&lt;/div&gt;
{% endif %}
&lt;p&gt;{{ config.SITE_ORGANISATION }}&lt;/p&gt;
```

</details>

---

## servicetask

> This variable is typically used as a loop iterator

<details>
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details>
<summary><strong>Properties</strong></summary>

| Property | Examples |
|----------|----------|
| `get_result_display.upper` | {{ servicetask.get_result_display.upper }} |
| `item` | {{ servicetask.item|bsecure_badge_code }} |
| `item.extra_fields.door_depth` | {{servicetask.item.extra_fields.door_depth}} |
| `item.extra_fields.door_width` | {{servicetask.item.extra_fields.door_width}} |
| `item.get_extra_fields_display.certification_id_present` | {{servicetask.item.get_extra_fields_display.certification_id_present}} |
| `item.get_extra_fields_display.comments` | {{servicetask.item.get_extra_fields_display.comments}} |
| `item.get_extra_fields_display.door_height` | {{servicetask.item.get_extra_fields_display.door_height}} |
| `item.get_extra_fields_display.door_material` | {{servicetask.item.get_extra_fields_display.door_material}} |
| `item.get_extra_fields_display.door_rating` | {{servicetask.item.get_extra_fields_display.door_rating}} |
| `item.get_extra_fields_display.frame_material` | {{servicetask.item.get_extra_fields_display.frame_material}} |
| `item.get_label` | {{ servicetask.item.get_label }} |
| `item.inspection_ref` | {{ servicetask.item.inspection_ref }} |
| `item.location` | {{ servicetask.item.location }} |
| `result` | {{ servicetask.result }} |

</details>

<details>
<summary><strong>Filters Used</strong></summary>

- `bsecure_badge_code`
- `bsecure_url`

</details>

<details>
<summary><strong>Usage Examples</strong></summary>

```django
&lt;tbody&gt;
&lt;tr class="keep-together bottom-border"&gt;
&lt;th width="35%" class="bg-white"&gt;{{ servicetask.item.get_label }}&lt;/th&gt;
&lt;th width="50%" class="bg-white light-text-weight"&gt;
{% if servicetask.item.inspection_ref %}
```

```django
&lt;th width="50%" class="bg-white light-text-weight"&gt;
{% if servicetask.item.inspection_ref %}
&lt;strong&gt;Serial:&lt;/strong&gt; {{ servicetask.item.inspection_ref }}
{% endif %}
{% if servicetask.item.bsecure_latest_sticker_guid %}
```

```django
{% endif %}
{% if servicetask.item.bsecure_latest_sticker_guid %}
&lt;a href="{{ servicetask.item|bsecure_url }}"&gt;
&lt;strong&gt;BSecure:&lt;/strong&gt; {{ servicetask.item|bsecure_badge_code }}
{% include "reports/library/arrow-up-right-from-square-icon.svg" with width="11" height="11" %}
```

</details>

---

## signoff

<details>
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details>
<summary><strong>Properties</strong></summary>

| Property | Examples |
|----------|----------|
| `account` | {{ signoff.account }} |
| `contractor` | {{ signoff.contractor }} |
| `period_finish` | {{ signoff.period_finish }} |
| `period_start` | {{ signoff.period_start}} |
| `pk` | {{ signoff.pk }} |

</details>

<details>
<summary><strong>Usage Examples</strong></summary>

```django
{% extends 'email.html' %}
{% block content %}
&lt;h3&gt;Contractor sign off {{ signoff.pk }} results for {{ signoff.contractor }}&lt;/h3&gt;
&lt;h4&gt;Submitted by {{ signoff.account }} for {{ signoff.period_start}} to {{ signoff.period_finish }}.&lt;/h4&gt;
{% for signoffproperty in signoff.signoffproperty_set.all %}
```

```django
{% block content %}
&lt;h3&gt;Contractor sign off {{ signoff.pk }} results for {{ signoff.contractor }}&lt;/h3&gt;
&lt;h4&gt;Submitted by {{ signoff.account }} for {{ signoff.period_start}} to {{ signoff.period_finish }}.&lt;/h4&gt;
{% for signoffproperty in signoff.signoffproperty_set.all %}
&lt;h5&gt;{{ signoffproperty.property }}&lt;/h5&gt;
```

</details>

---

## signoffitem

> This variable is typically used as a loop iterator

<details>
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details>
<summary><strong>Properties</strong></summary>

| Property | Examples |
|----------|----------|
| `label` | {{ signoffitem.label }} |
| `new_serviced_date` | {{ signoffitem.new_serviced_date }} |
| `new_signoff_note` | {{ signoffitem.new_signoff_note }} |

</details>

<details>
<summary><strong>Usage Examples</strong></summary>

```django
{% endif %}
]
{{ signoffitem.label }}
{% if signoffitem.new_signoff_note %}
&lt;div style="color: blue"&gt;Note: {{ signoffitem.new_signoff_note }}&lt;/div&gt;
```

```django
{{ signoffitem.label }}
{% if signoffitem.new_signoff_note %}
&lt;div style="color: blue"&gt;Note: {{ signoffitem.new_signoff_note }}&lt;/div&gt;
{% endif %}
{% if signoffitem.new_serviced_date %}
```

```django
{% endif %}
{% if signoffitem.new_serviced_date %}
&lt;div style="color: #666"&gt;Service date: {{ signoffitem.new_serviced_date }}&lt;/div&gt;
{% endif %}
&lt;/li&gt;
```

</details>

---

## signoffproperties

<details>
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details>
<summary><strong>Filters Used</strong></summary>

- `pluralize`

</details>

<details>
<summary><strong>Usage Examples</strong></summary>

```django
{% extends 'email.html' %}
{% block content %}
&lt;h4&gt;Request{{ signoffproperties|pluralize }} for {{ contractor.name }} ({{ contractor.account }}).&lt;/h4&gt;
&lt;p&gt;In order to issue compliant reports, we require confirmation that you, as a service contractor, have serviced the relevant Essential Safety Measures to Australian Standards over the previous 12 months.&lt;/p&gt;
&lt;table border="0" cellpadding="10" cellspacing="0" bgcolor="#27a9e3" width="100%"&gt;
```

```django
{% endfor %}
&lt;/ul&gt;
&lt;p&gt;If the form{{ signoffproperties|pluralize }} on the attached link {{ signoffproperties|pluralize:"is,are" }} not submitted within the next 30 days and there is no proof on site that the Essential Safety Measures are being serviced, {{ signoffproperties|pluralize:"a," }} Non-Compliant Building Report{{ signoffproperties|pluralize }} will be issued.&lt;/p&gt;
{% endblock %}
{% extends 'email.html' %}
```

```django
{% endfor %}
&lt;/ul&gt;
&lt;p&gt;If the form{{ signoffproperties|pluralize }} on the attached link {{ signoffproperties|pluralize:"is,are" }} not submitted and there is no proof on site that the Essential Safety Measures are being serviced, {{ signoffproperties|pluralize:"a," }} Non-Compliant Building Report{{ signoffproperties|pluralize }} will be issued.&lt;/p&gt;
{% endblock %}
&lt;p&gt;Dear {{ client.primary_contact.name }},&lt;/p&gt;
```

</details>

---

## signoffproperty

> This variable is typically used as a loop iterator

<details>
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details>
<summary><strong>Properties</strong></summary>

| Property | Examples |
|----------|----------|
| `created` | {{ signoffproperty.created|date }} |
| `disclaimed_reason` | {{signoffproperty.disclaimed_reason}} |
| `due` | {{ signoffproperty.due|date }} |
| `is_disclaimed` | {{ signoffproperty.is_disclaimed }} |
| `note` | {{ signoffproperty.note }} |
| `property` | {{ signoffproperty.property }} |
| `property.name` | {{ signoffproperty.property.name }} |

</details>

<details>
<summary><strong>Filters Used</strong></summary>

- `date`

</details>

<details>
<summary><strong>Usage Examples</strong></summary>

```django
{% for signoffproperty in signoffproperties %}
&lt;li&gt;
&lt;h5&gt;{{ signoffproperty.property.name }}&lt;/h5&gt;
&lt;p&gt;
Due: {{ signoffproperty.due|date }}
```

```django
&lt;h5&gt;{{ signoffproperty.property.name }}&lt;/h5&gt;
&lt;p&gt;
Due: {{ signoffproperty.due|date }}
&lt;/p&gt;
&lt;/li&gt;
```

```django
{% for signoffproperty in signoffproperties %}
&lt;li&gt;
&lt;h5&gt;{{ signoffproperty.property.name }}&lt;/h5&gt;
&lt;p&gt;
Due: {{ signoffproperty.due|date }}&lt;br/&gt;
```

</details>

---

## start_date

<details>
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details>
<summary><strong>Usage Examples</strong></summary>

```django
&lt;tr&gt;
&lt;td style="border: 3px double #000; padding: 8px; width: 25%; background-color: #f0f0f0;"&gt;START DATE&lt;/td&gt;
&lt;td style="border: 3px double #000; padding: 8px; width: 25%;"&gt;{{start_date}}&lt;/td&gt;
&lt;td style="border: 3px double #000; padding: 8px; width: 25%; background-color: #f0f0f0;"&gt;END DATE&lt;/td&gt;
&lt;td style="border: 3px double #000; padding: 8px; width: 25%;"&gt;{{end_date}}&lt;/td&gt;
```

</details>

---

## subject

<details>
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details>
<summary><strong>Usage Examples</strong></summary>

```django
To: {{ to_list }}&lt;br /&gt;
CC: {{ cc_list }}&lt;br /&gt;
Subject {{ subject }}&lt;br /&gt;
&lt;/p&gt;
&lt;p&gt;
```

```django
Address: {{ bounce_address }}&lt;br /&gt;
Bounce Reason: {{ formatted_reason }}&lt;br /&gt;
Email Subject {{ subject }}&lt;br /&gt;
Email Sent: {{ formatted_timestamp }}
&lt;/p&gt;
```

</details>

---

## task

> This variable is typically used as a loop iterator

<details>
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details>
<summary><strong>Properties</strong></summary>

| Property | Examples |
|----------|----------|
| `address` | {{ task.address }} |
| `description` | {{ task.description }} |
| `name` | {{ task.name }} |
| `property.name` | {{ task.property.name }} |
| `ref` | {{ task.ref }} |

</details>

<details>
<summary><strong>Usage Examples</strong></summary>

```django
{% endblock %}
&lt;p&gt;Dear {{ attention }},&lt;/p&gt;
&lt;p&gt;Please find attached our purchase order{% if task %} for {{ task.name }}{% endif %}.&lt;/p&gt;
&lt;p&gt;Please deliver the parts to {{purchaseorder.delivery_instructions}} &lt;/p&gt;
&lt;p&gt;&lt;strong&gt;Delivery Address:&lt;strong&gt;&lt;/p&gt;
```

```django
{% for task in tasks %}
&lt;p&gt;
Task {{ task.ref }}&lt;br&gt;
{{ task.description }}&lt;br&gt;
{{ task.property.name }}&lt;br&gt;
```

```django
&lt;p&gt;
Task {{ task.ref }}&lt;br&gt;
{{ task.description }}&lt;br&gt;
{{ task.property.name }}&lt;br&gt;
{{ task.address }}
```

</details>

---

## task_origin_defectquote

<details>
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details>
<summary><strong>Properties</strong></summary>

| Property | Examples |
|----------|----------|
| `status` | {{ task_origin_defectquote.status }} |
| `status.upper` | {{ task_origin_defectquote.status.upper }} |

</details>

<details>
<summary><strong>Usage Examples</strong></summary>

```django
{% include "reports/library/arrow-up-right-from-square-icon.svg" with width="14" height="14" %}
&lt;/a&gt;
&lt;div class="status quote {{ task_origin_defectquote.status }} ml-2 mt-1"&gt;
{{ task_origin_defectquote.status.upper }}
&lt;/div&gt;
```

```django
&lt;/a&gt;
&lt;div class="status quote {{ task_origin_defectquote.status }} ml-2 mt-1"&gt;
{{ task_origin_defectquote.status.upper }}
&lt;/div&gt;
&lt;/div&gt;
```

</details>

---

## task_quote

<details>
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details>
<summary><strong>Properties</strong></summary>

| Property | Examples |
|----------|----------|
| `get_uuid_approval_url` | {{ task_quote.get_uuid_approval_url|absolute }} |
| `ref` | {{ task_quote.ref }} |

</details>

<details>
<summary><strong>Filters Used</strong></summary>

- `absolute`

</details>

<details>
<summary><strong>Usage Examples</strong></summary>

```django
{% if task_quote.ref %}
&lt;div class="subtitle d-flex flex-row"&gt;
&lt;a href="{{ task_quote.get_uuid_approval_url|absolute }}"&gt;
{{ task_quote.ref }}
{% include "reports/library/arrow-up-right-from-square-icon.svg" with width="14" height="14" %}
```

```django
&lt;div class="subtitle d-flex flex-row"&gt;
&lt;a href="{{ task_quote.get_uuid_approval_url|absolute }}"&gt;
{{ task_quote.ref }}
{% include "reports/library/arrow-up-right-from-square-icon.svg" with width="14" height="14" %}
&lt;/a&gt;
```

</details>

---

## tasksession

<details>
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details>
<summary><strong>Properties</strong></summary>

| Property | Examples |
|----------|----------|
| `id` | {{ tasksession.id }} |
| `technician.name` | {{ tasksession.technician.name }} |

</details>

<details>
<summary><strong>Usage Examples</strong></summary>

```django
&lt;/p&gt;
&lt;p&gt;Thanks&lt;/p&gt;
&lt;p&gt;Task Session {{ tasksession.id }} encountered an error while syncing to the accounting partner.&lt;/p&gt;
{% if task %}
&lt;p&gt;&lt;b&gt;Task:&lt;/b&gt; {{ task }}&lt;/p&gt;
```

```django
&lt;p&gt;&lt;b&gt;Task:&lt;/b&gt; {{ task }}&lt;/p&gt;
{% endif %}
&lt;p&gt;&lt;b&gt;Technician:&lt;/b&gt; {{ tasksession.technician.name }}&lt;/p&gt;
&lt;p&gt;Please review and address the error, then use the link below to retry the sync&lt;/p&gt;
&lt;p&gt;
```

</details>

---

## template

<details>
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details>
<summary><strong>Usage Examples</strong></summary>

```django
&lt;p&gt;
Change request: &lt;a href="{{ base_url }}{{ changerequest.get_absolute_url }}"&gt;{{ changerequest.ref }}&lt;/a&gt;&lt;br /&gt;
Template: {% if template %}{{ template }}{% else %}New Template{% endif %}&lt;br /&gt;
Status: {{ changerequest.status }}
&lt;/p&gt;&lt;p&gt;Dear {{ client.name|default:'valued customer' }},&lt;/p&gt;
```

</details>

---

## title

<details>
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details>
<summary><strong>Usage Examples</strong></summary>

```django
&lt;div&gt;
&lt;div class="uptick-heading d-flex flex-row justify-content-between w-100 no-page-break-after"&gt;
&lt;div&gt;{{ title }}&lt;/div&gt;
{% if task_quote.ref %}
&lt;div class="subtitle d-flex flex-row"&gt;
```

</details>

---

## to_list

<details>
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details>
<summary><strong>Usage Examples</strong></summary>

```django
Email info:&lt;br /&gt;
Sent: {{ failure_datetime }}&lt;br /&gt;
To: {{ to_list }}&lt;br /&gt;
CC: {{ cc_list }}&lt;br /&gt;
Subject {{ subject }}&lt;br /&gt;
```

</details>

---

## url

<details>
<summary><strong>Found in files</strong></summary>

- generic.txt

</details>

<details>
<summary><strong>Usage Examples</strong></summary>

```django
&lt;p&gt;A new message from {{ from }} is waiting for you:&lt;/p&gt;
&lt;p&gt;{{ chat_message.text }}&lt;/p&gt;
&lt;p&gt;{{ base_url }}{{ url }}&lt;/p&gt;
&lt;p&gt;Regards, &lt;br/&gt;
{{ config.SITE_ORGANISATION }}
```

</details>

---


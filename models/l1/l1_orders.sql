{{ config(
    materialized='incremental',
    unique_key='order_id'
) }}

SELECT
    order_id,
    customer_id,
    amount,
    status,
    created_at,
    updated_at,
    current_timestamp() AS dw_insert_ts
FROM {{ source('raw', 'orders') }}

{% if is_incremental() %}
WHERE updated_at > (SELECT max(updated_at) FROM {{ this }})
{% endif %}

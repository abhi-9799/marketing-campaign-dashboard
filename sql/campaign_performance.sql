SELECT
  trafficSource.campaign AS campaign_name,
  COUNT(visitId) AS sessions,
  SUM(totals.transactions) AS transactions,
  SUM(totals.transactionRevenue)/1000000 AS revenue_usd,
  SUM(trafficSource.adwordsClickInfo.page) AS clicks
FROM `bigquery-public-data.google_analytics_sample.ga_sessions_*`
WHERE _TABLE_SUFFIX BETWEEN '20170101' AND '20170131'
GROUP BY campaign_name
ORDER BY revenue_usd DESC;

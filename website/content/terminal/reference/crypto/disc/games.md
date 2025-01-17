---
title: games
description: This page provides a list of top blockchain games with sorting options
  by Name, Daily Users, and Daily Volume. Use this command to discover the most popular
  and lucrative blockchain games.
keywords:
- blockchain
- blockchain games
- crypto games
- daily volume
- daily users
- sorting
- top games
- Splinterlands
- PancakeSwap
- Alien Worlds
- Axie Infinity
- OpenSea
---

import HeadTitle from '@site/src/components/General/HeadTitle.tsx';

<HeadTitle title="crypto/disc/games - Reference | OpenBB Terminal Docs" />

Shows top blockchain games [Source: https://dappradar.com/] Accepts --sort {Name,Daily Users,Daily Volume [$]} to sort by column

### Usage

```python
games [-l LIMIT] [-s SORTBY [SORTBY ...]]
```

---

## Parameters

| Name | Description | Default | Optional | Choices |
| ---- | ----------- | ------- | -------- | ------- |
| limit | Number of records to display | 15 | True | None |
| sortby | Sort by given column. Default: Daily Volume [$] | Daily Volume [$] | True | Name, Category, Daily Users, Daily Volume [$] |


---

## Examples

```python
2022 Feb 15, 06:53 (🦋) /crypto/disc/ $ games
               Top Blockchain Games
┌───────────────┬─────────────┬──────────────────┐
│ Name          │ Daily Users │ Daily Volume [$] │
├───────────────┼─────────────┼──────────────────┤
│ Splinterlands │ 305.1K      │ 8K               │
├───────────────┼─────────────┼──────────────────┤
│ PancakeSwap   │ 289.3K      │ 223.7M           │
├───────────────┼─────────────┼──────────────────┤
│ Alien Worlds  │ 235.6K      │ 759.2K           │
├───────────────┼─────────────┼──────────────────┤
│ Farmers World │ 111.7K      │ 2.3K             │
├───────────────┼─────────────┼──────────────────┤
│ AtomicAssets  │ 108.9K      │ 226.3K           │
├───────────────┼─────────────┼──────────────────┤
│ Axie Infinity │ 90.9K       │ 11.6M            │
├───────────────┼─────────────┼──────────────────┤
│ Upland        │ 63.3K       │ 0                │
├───────────────┼─────────────┼──────────────────┤
│ OpenSea       │ 54K         │ 200M             │
├───────────────┼─────────────┼──────────────────┤
│ Katana        │ 45.9K       │ 92.7M            │
├───────────────┼─────────────┼──────────────────┤
│ Magic Eden    │ 40.2K       │ 18.5M            │
└───────────────┴─────────────┴──────────────────┘
```
---

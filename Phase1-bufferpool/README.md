# 📦 Buffer Pool Implementation with Pluggable Replacement Policies

This project implements a **Buffer Pool Manager** that supports multiple page replacement policies using a **modular design**.

## 🚀 Supported Replacement Policies

* **LRU (Least Recently Used)**
* **LRU-K (Generalized LRU using K-th recent access)**

---

# 🧠 Design Approach — External Policy Classes with Independent Metadata

This implementation follows a **clean separation of concerns**:

### 🔹 BufferPool Responsibilities

* Stores pages in memory (`frames`)
* Maintains a lookup structure (`page_table`)
* Handles:

  * Page fetch requests
  * Insertions and removals
  * Buffer capacity management

### 🔹 Policy Responsibilities

Each replacement policy:

* Maintains its **own metadata**
* Does **NOT directly modify buffer contents**
* Provides decisions to the buffer

---

## 🔁 Interaction Between BufferPool and Policy

The interaction is based on a simple contract:

### On page access (HIT)

```python
policy.record_access(page_id)
```

### On page insertion (MISS)

```python
policy.record_insert(page_id)
```

### On eviction

```python
victim = policy.choose_victim(current_frames)
```

### On removal

```python
policy.record_removal(page_id)
```

---

# 🧩 Architecture Overview

```
          +---------------------+
          |     BufferPool      |
          |---------------------|
          | frames              |
          | page_table          |
          | policy              |
          +----------+----------+
                     |
                     | calls
                     ↓
        +---------------------------+
        |   Replacement Policy      |
        |---------------------------|
        | metadata (policy-specific)|
        | record_access()           |
        | record_insert()           |
        | choose_victim()           |
        | record_removal()          |
        +---------------------------+
```

---

# 📊 Replacement Policies

## 🔹 LRU (Least Recently Used)

* Tracks recency using an ordered structure (e.g., `OrderedDict`)
* On access:

  * Page is moved to the most recent position
* Eviction:

  * Removes the least recently used page

### ✔ Characteristics

* Simple and efficient
* Works well for temporal locality

---

## 🔹 LRU-K

* Tracks the **last K access timestamps** for each page
* Eviction decision:

  * Based on the **K-th most recent access**
* Pages with fewer than K accesses are considered weaker candidates

### ✔ Example (K = 2)

| Page | Access History | Score (2nd last) |
| ---- | -------------- | ---------------- |
| A    | [2, 10]        | 2                |
| B    | [4, 9]         | 4                |

➡️ Page **A** is evicted (older 2nd access)

### ✔ Characteristics

* More robust than LRU
* Reduces impact of one-time accesses
* Better for distinguishing frequently used pages

---

# ⚙️ Key Features

* ✅ Modular and extensible design
* ✅ Easy to plug in new policies (e.g., LFU, Clock)
* ✅ Clear separation between data storage and decision logic
* ✅ Supports comparative experimentation between policies

---

# 🧪 Example Usage

```python
pool = BufferPool(size=3, policy=LRUKPolicy(k=2))

pages = [1, 2, 3, 1, 2, 4, 5]

for p in pages:
    pool.fetch_page(p)
    pool.display()
```

---

# 🏗️ Extending the System

To add a new replacement policy:

1. Create a new class:

```python
class NewPolicy:
    def record_access(self, page_id): ...
    def record_insert(self, page_id): ...
    def choose_victim(self, frames): ...
    def record_removal(self, page_id): ...
```

2. Pass it to the buffer pool:

```python
pool = BufferPool(size=3, policy=NewPolicy())
```

---

# 📌 Summary

This implementation demonstrates a **clean, extensible buffer management system** where:

* The **BufferPool manages data**
* The **Policy decides behavior**
* Both are **loosely coupled**

This design closely reflects real-world database systems and allows easy experimentation with different eviction strategies.
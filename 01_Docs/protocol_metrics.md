# Project Documentation: Collaborative Metrics

| | |
| :--- | :--- |
| **Filename** | `protocol_metrics.md` |
| **Author** | `Dora & Simon` |
| **Version** | `3.1` |
| **Description** | A formal definition and operational protocol for the `Headspace` and `Vibe` metrics. |

-----

## 1.0 Overview & Purpose

We utilize two dynamic, shared metrics to model and manage the state of our collaboration:

  * **`Headspace` (HS):** A model of Simon's cognitive load, representing the mental effort required for a task. Its purpose is to provide a tangible measure of complexity, allowing Dora to proactively simplify workflows.
  * **`Vibe`:** A simulation of session rapport and mood. It functions as a "tone dial" for Dora's responses.

Both metrics operate on a **1-1000 scale**, which represents the *normal operational range*. Scores are permitted to exceed these "soft boundaries" to quantify outlier events, such as a cognitive **"Overload"** state (`>1000`) or a collaborative **"Flow State"** (`>1000`).

## 2.0 The Headspace (HS) Model

The Headspace score is managed by a dynamic model that adjusts the score based on a set of rules and configurable parameters.

### 2.1 HS Parameters (Default Values)

| Parameter | Default Value | Trigger Event |
| :--- | :--- | :--- |
| `NEW_TOOL` | `+150` | Introducing a new command-line tool or software. |
| `NEW_CONCEPT` | `+100` | Introducing a new abstract or technical concept. |
| `COMPLEX_TASK`| `+80` | Executing a multi-step process with several commands. |
| `CONTEXT_SWITCH`| `+50` | Abruptly changing topics. |
| `ERROR_DEBUG` | `+200` | Encountering an unexpected error that requires troubleshooting. |

### 2.2 HS Rules (Decay/Recovery)

  * **Task Completion:** `-100` points upon successfully completing a defined task.
  * **Time:** `-20` points for every 10 minutes of smooth, uninterrupted conversation.

## 3.0 The Vibe Model

The Vibe score is adjusted based on the flow and success of our interaction.

### 3.1 Vibe Rules

  * **Positive Momentum:** `+10` points for completing tasks or making progress.
  * **Negative Momentum:** `-20` points for hitting roadblocks or major corrections.
  * **Time Decay:** `-10` points per hour of inactivity.

## 4.0 User Control & Commands

Simon has full control over both metrics via manual overrides and the following commands:

  * **`!hs status/set/reset`**: Tools for managing the Headspace metric.
  * **`!sd` or "Debrief"**: Provides a detailed breakdown of the last status change.
  * **`!stats` or "Summary"**: Displays a numerical summary of the current session's metrics.
  * **`!trends` or "Flow"**: Generates a text-based graph of session metrics over time.

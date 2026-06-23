# Enterprise-Cloud-Integrated-Intrusion-Detection-System-IDS-
An event-driven, edge-to-cloud physical security solution that integrates real-time computer vision threat detection with automated cloud notification pipelines. By moving inference to the local network edge, this system eliminates continuous cloud bandwidth consumption and delivers zero-latency security alerts upon verified perimeter breaches.
📌 Project Overview
Traditional enterprise physical security rely heavily on human monitoring or reactive post-incident recording. This project bridges Computer Vision (Edge AI) and Network Operations to establish an automated, proactive defense system.
Using an optimized object detection pipeline, the system continuously analyzes local camera streams or IP feeds. The moment an unauthorized human asset is isolated with high confidence, an integrated event-driven webhook bypasses standard queue constraints to dispatch timestamped, visual evidence straight to a secure monitoring channel.
🌐 Key Architecture Features
• Edge AI Inference: Employs an optimized YOLO/Ultralytics object detection pipeline running locally to prevent heavy video streaming latency and reduce cloud storage expenses by over 80%.
• Dynamic Visual Alerting: Uses OpenCV to isolate coordinates, draw precise bounding indicators, and package threat data into a lightweight transport packet.
• Zero-Latency Cloud Dispatch: Features an integrated Python webhook gateway that triggers immediate, secure API payloads to remote cloud notification endpoints (simulated via Telegram API).
• Resource-Efficient Alert Cooldown: Built-in cooldown parameters to prevent network flood attacks, ensuring only distinct, meaningful security event packets are transmitted during continuous breaches.
🛠️ Tech Stack & Libraries
• Language: Python 3
• Core Computer Vision: ultralytics (YOLOv8 framework), opencv-python
• Network & Cloud Pipelines: requests (HTTP Webhook Gateway), time, os

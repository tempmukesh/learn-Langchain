from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(
    model = "gemini-2.5-flash",
    temperature=0.0,

)

output  = model.invoke("What is system design ?")

# output have 
# 1. content 
# 2. metadata 


result = output.content

print(result)

# **System design** is the process of defining the architecture, components, modules, interfaces, and data for a system to satisfy specified requirements. It's essentially the blueprint for how a software system will be built, outlining its structure, behavior, and interactions.

# Think of it like an architect designing a building:
# *   They don't just start laying bricks; they first create detailed plans.
# *   They consider the purpose of the building, the number of occupants, the budget, the materials, the plumbing, electrical systems, and how everything will fit together.
# *   System design does the same for software.

# ### Why is System Design Important?

# 1.  **Problem Solving:** It ensures the proposed system effectively solves the real-world problem it's intended for.
# 2.  **Blueprint for Development:** Provides a clear roadmap for developers, reducing ambiguity and rework.
# 3.  **Efficiency and Performance:** Helps optimize resource usage, ensuring the system runs fast and efficiently.
# 4.  **Scalability:** Designs the system to handle increased load (more users, more data) in the future without major overhauls.
# 5.  **Reliability and Availability:** Plans for fault tolerance and redundancy to ensure the system remains operational even if parts fail.
# 6.  **Maintainability:** Makes the system easier to understand, update, and fix bugs in the long run.
# 7.  **Cost-Effectiveness:** Helps choose appropriate technologies and infrastructure to stay within budget.
# 8.  **Security:** Integrates security measures from the ground up to protect data and prevent unauthorized access.
# 9.  **Collaboration:** Facilitates communication and understanding among different teams (developers, operations, product managers).

# ### Key Aspects and Considerations in System Design:

# When designing a system, engineers consider various factors, often categorized into:

# **1. Requirements Analysis:**
#     *   **Functional Requirements:** What the system *must do* (e.g., "Users can log in," "The system can process payments").
#     *   **Non-Functional Requirements (NFRs):** How well the system performs its functions (e.g., "The system must handle 1 million users concurrently," "Login must complete in under 2 seconds," "Data must be encrypted"). These are crucial for design decisions.

# **2. Architectural Style:**
#     *   **Monolithic:** A single, unified codebase.
#     *   **Microservices:** Breaking down the system into small, independent services.
#     *   **Serverless:** Relying on cloud providers to manage infrastructure.
#     *   **Event-Driven:** Systems that react to events.

# **3. Component Identification:**
#     *   **Databases:** Choosing the right type (SQL, NoSQL) and schema.
#     *   **APIs (Application Programming Interfaces):** How different parts of the system (and external systems) communicate.
#     *   **Load Balancers:** Distributing incoming traffic across multiple servers.
#     *   **Caches:** Storing frequently accessed data for faster retrieval.
#     *   **Message Queues:** For asynchronous communication between services.
#     *   **Authentication/Authorization Services:** Managing user access and permissions.
#     *   **Storage Solutions:** For files, media, etc.

# **4. Data Management:**
#     *   **Data Modeling:** Designing the structure of data.
#     *   **Data Storage:** Where and how data is persisted.
#     *   **Data Consistency:** Ensuring data remains accurate across distributed systems.
#     *   **Data Backup and Recovery:** Strategies for disaster recovery.

# **5. Scalability Strategies:**
#     *   **Vertical Scaling:** Adding more resources (CPU, RAM) to a single server.
#     *   **Horizontal Scaling:** Adding more servers to distribute the load.
#     *   **Sharding/Partitioning:** Dividing data across multiple databases.

# **6. Reliability and Fault Tolerance:**
#     *   **Redundancy:** Having backup components.
#     *   **Failover Mechanisms:** Automatically switching to a backup if a primary component fails.
#     *   **Circuit Breakers:** Preventing cascading failures in microservices.

# **7. Security:**
#     *   **Authentication:** Verifying user identity.
#     *   **Authorization:** Determining what an authenticated user can do.
#     *   **Encryption:** Protecting data in transit and at rest.
#     *   **Access Control:** Limiting who can access what.

# **8. Monitoring and Logging:**
#     *   Tools and strategies to observe system health, performance, and troubleshoot issues.

# **9. Deployment and Operations:**
#     *   How the system will be deployed, managed, and updated in production.

# ### Who Does System Design?

# System design is primarily done by **System Architects** and **Senior Software Engineers**. They leverage their experience and understanding of various technologies to create robust, scalable, and maintainable solutions. It's often an iterative process, evolving as requirements change and new technologies emerge.
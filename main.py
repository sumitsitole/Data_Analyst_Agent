from agent import root_agent

if __name__ == "__main__":
    from google.adk.runners import Runner
    from google.adk.sessions import InMemorySessionService
    import asyncio

    session_service = InMemorySessionService()
    runner = Runner(agent=root_agent, app_name="data_analyst", session_service=session_service)

    print("Data Analyst Agent is running...")

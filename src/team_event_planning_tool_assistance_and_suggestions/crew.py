from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import WebsiteSearchTool
from crewai_tools import ScrapeWebsiteTool

@CrewBase
class TeamEventPlanningToolAssistanceAndSuggestionsCrew():
    """TeamEventPlanningToolAssistanceAndSuggestions crew"""

    @agent
    def venue_search_expert(self) -> Agent:
        return Agent(
            config=self.agents_config['venue_search_expert'],
            tools=[WebsiteSearchTool()],
        )

    @agent
    def detail_extraction_specialist(self) -> Agent:
        return Agent(
            config=self.agents_config['detail_extraction_specialist'],
            tools=[ScrapeWebsiteTool()],
        )

    @agent
    def event_evaluation_consultant(self) -> Agent:
        return Agent(
            config=self.agents_config['event_evaluation_consultant'],
            
        )


    @task
    def search_venues_task(self) -> Task:
        return Task(
            config=self.tasks_config['search_venues_task'],
            tools=[WebsiteSearchTool()],
        )

    @task
    def extract_event_details_task(self) -> Task:
        return Task(
            config=self.tasks_config['extract_event_details_task'],
            tools=[ScrapeWebsiteTool()],
        )

    @task
    def evaluate_and_suggest_events_task(self) -> Task:
        return Task(
            config=self.tasks_config['evaluate_and_suggest_events_task'],
            
        )


    @crew
    def crew(self) -> Crew:
        """Creates the TeamEventPlanningToolAssistanceAndSuggestions crew"""
        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )

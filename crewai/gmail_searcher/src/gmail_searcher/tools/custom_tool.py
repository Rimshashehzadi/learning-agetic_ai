# from typing import Type

# from crewai.tools import BaseTool
# from pydantic import BaseModel, Field


# class MyCustomToolInput(BaseModel):
#     """Input schema for MyCustomTool."""

#     argument: str = Field(..., description="Description of the argument.")


# class MyCustomTool(BaseTool):
#     name: str = "Name of my tool"
#     description: str = (
#         "Clear description for what this tool is useful for, your agent will need this information to use it."
#     )
#     args_schema: Type[BaseModel] = MyCustomToolInput

#     def _run(self, argument: str) -> str:
#         # Implementation goes here
#         return "this is an example of a tool output, ignore it and move along."

# Create a PDF knowledge source
from crewai.knowledge.source.pdf_knowledge_source import PDFKnowledgeSource
pdf_source = PDFKnowledgeSource(
    file_paths=["C:\Users\Computer World\Documents"]
)
from dataclasses import dataclass, field


@dataclass
class DeveloperMetrics:
    pointsClosed: float = 0
    percentContribution: float = 0  # points / (totalPoints) * %100


@dataclass
class MilestoneData:
    totalPointsClosed: float = 0
    devMetrics: dict[str, DeveloperMetrics] = field(default_factory=dict)


@dataclass
class LectureTopicTaskData:
    totalLectureTopicTasks: int = 0
    lectureTopicTasksByDeveloper: dict[str, int] = field(default_factory=dict)

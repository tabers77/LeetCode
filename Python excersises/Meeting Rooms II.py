import heapq


def minMeetingRooms(intervals) -> int:
    # If there is no meeting to schedule then no room needs to be allocated.

    if not intervals:
        return 0

    # The heap initialization
    free_rooms = []

    # Sort the meetings in increasing order of their start time.
    intervals.sort(key=lambda x: x[0])

    # Add the first meeting. We have to give a new room to the first meeting.
    # This will add the end hour of first meeting
    heapq.heappush(free_rooms, intervals[0][1])

    # For all the remaining meeting rooms
    for meeting in intervals[1:]:

        # If the room due to free up the earliest is free, assign that room to this meeting.
        # Ex: [[2, 11], [6, 16], [11, 16]] here it will check 11 in the first meeting and 11 in the third meeting
        if free_rooms[0] <= meeting[0]:
            heapq.heappop(free_rooms)

        # If a new room is to be assigned, then also we add to the heap,
        # If an old room is allocated, then also we have to add to the heap with updated end time.
        heapq.heappush(free_rooms, meeting[1])

    # The size of the heap tells us the minimum rooms required for all the meetings.
    return len(free_rooms)


intervals_input = [[2, 11], [6, 16], [11, 16]]
print(minMeetingRooms(intervals_input))


# WRONG ANSWER
def minMeetingRooms(intervals) -> int:
    """
    Logic
    ------
    higher or equal than first prior lower or equals than sencond prior
    lower or equals than second
    """
    sorted_intervals = sorted(intervals, key=lambda x: (x[0], -x[1]))
    print(sorted_intervals)
    # sorted_intervals = sorted(intervals, key=lambda x: x[0])
    # sorted_intervals = sorted(sorted_intervals, key=lambda x: x[1], reverse=True)
    # return  sorted_intervals
    # sorted_intervals = sorted(intervals)

    n_rooms = 1
    print(sorted_intervals)
    for idx, interval in enumerate(sorted_intervals):
        if idx < len(sorted_intervals) - 1:
            if sorted_intervals[idx + 1][0] >= sorted_intervals[idx][0] and sorted_intervals[idx + 1][0] < \
                    sorted_intervals[idx][1]:
                n_rooms += 1
            elif sorted_intervals[idx + 1][1] <= sorted_intervals[idx][1]:
                n_rooms += 1
    return n_rooms

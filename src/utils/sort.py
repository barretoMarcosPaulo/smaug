class SortValues:
    def __init__(self, values):
        self.values = values

    def _partition(self, start, end, dict_field):
        pivot = start
        for i in range(start+1, end+1):
            if dict_field:
                if self.values[i][dict_field] <= self.values[start][dict_field]:
                    pivot += 1
                    self.values[i], self.values[pivot] = self.values[pivot], self.values[i]
            else:
                if self.values[i] <= self.values[start]:
                    pivot += 1
                    self.values[i], self.values[pivot] = self.values[pivot], self.values[i]

        self.values[pivot], self.values[start] = self.values[start], self.values[pivot]
        return pivot


    def sort_elements(self, start=0, end=None, dict_field=False):
        if end is None:
            end = len(self.values) - 1
        if start >= end:
            return self.values
        pivot = self._partition(start, end, dict_field)
        self.sort_elements(start, pivot-1, dict_field)
        self.sort_elements(pivot+1, end, dict_field)


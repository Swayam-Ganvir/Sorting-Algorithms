from tkinter import *
import matplotlib.animation
import matplotlib.pyplot as plt
import random
import math
import matplotlib.animation as animation

class MyButton:
    def __init__(self, root):
        self.f = Frame(root, height=400, width=500, bg="#005F73",)
        
        self.f.propagate(0)

        self.f.pack()
        
        self.b1 = Button(self.f, text="1) BUBBLE SORT", width=15, height=2, padx=20, pady=10, command=self.bubble_sort, relief='solid', bg="#94D2BD",font=('bold'))
        self.b2 = Button(self.f, text="2) SELECTION SORT", width=15, height=2,padx=20, pady=10, command=self.selection_sort,relief='solid',bg="#94D2BD",font=('bold'))
        self.b3 = Button(self.f, text="3) INSERTION SORT", width=15, height=2,padx=20, pady=10, command=self.insertion_sort,relief='solid',bg="#94D2BD",font=('bold'))
        self.b4 = Button(self.f, text="4) BUCKED SORT", width=15, height=2, padx=20, pady=10, command=self.bucket_sort,relief='solid',bg="#94D2BD",font=('bold'))
        self.b5 = Button(self.f, text="5) MERGE SORT", width=15, height=2, padx=20, pady=10, command=self.merge_sort,relief='solid',bg="#94D2BD",font=('bold'))
        self.b6 = Button(self.f, text="6) QUICK SORT", width=15, height=2, padx=20, pady=10, command=self.quick_sort,relief='solid',bg="#94D2BD",font=('bold'))
        
        
        self.b1.grid_configure(row=0, column=0, padx=10, pady=15)
        self.b2.grid_configure(row=1, column=0, padx=10, pady=15)
        self.b3.grid_configure(row=2, column=0, padx=10, pady=15)
        self.b4.grid_configure(row=3, column=0, padx=10, pady=15)
        self.b5.grid_configure(row=0, column=1,padx=10, pady=15)
        self.b6.grid_configure(row=1, column=1,padx=10, pady=15)

    
    def bubble_sort(self):
        def bubbleSort(customList):
            for i in range(len(customList)-1):
                for j in range(len(customList) - i - 1):
                    if customList[j] > customList[j+1]:
                        customList[j], customList[j+1] = customList[j+1], customList[j]
                    yield customList

        def visualize_bubble_sort(customList):
            fig, ax = plt.subplots()
            bar_rects = ax.bar(range(len(customList)), customList, align="edge")
            ax.set_xlim(0, len(customList))
            ax.set_ylim(0, 1.1*max(customList))

            def update_bars(array, rects):
                for rect, val in zip(rects, array):
                    rect.set_height(val)
            
            generator = bubbleSort(customList)
            
            def animate(frame):
                array = next(generator)
                update_bars(array, bar_rects)
                
            ani = matplotlib.animation.FuncAnimation(fig, animate, frames=range(len(customList)*len(customList)), repeat=False, interval=20)
            plt.show()

        customList = random.sample(range(1, 100), 20)
        visualize_bubble_sort(customList)
    
    def selection_sort(self):
        def selectionSort(customList):
            for i in range(len(customList)):
                min_index = i
                for j in range(i+1, len(customList)):
                    if customList[min_index] > customList[j]:
                        min_index = j
                customList[i] , customList[min_index] = customList[min_index], customList[i]
                yield customList
            
        def visulize_selection_sort(customList):
            fig, ax = plt.subplots()
            bar_rects = ax.bar(range(len(customList)),customList ,align="edge")
            ax.set_xlim(0, len(customList))
            ax.set_ylim(0, 1.1*max(customList))
                
            def update_bars(array, rects):
                for rect, val in zip(rects, array):
                    rect.set_height(val)
            
            generator = selectionSort(customList)
            
            def animate(frame):
                array = next(generator)
                update_bars(array, bar_rects)
            
            ani = matplotlib.animation.FuncAnimation(fig, animate, frames=range(len(customList)*len(customList)), repeat=False, interval=200)
            plt.show()
                
        random_array = random.sample(range(1,100),20)
        visulize_selection_sort(random_array)
    
    def insertion_sort(self):
        def insertion_sort(customList):
            for i in range(1, len(customList)):
                key = customList[i]
                j = i - 1
                while j >= 0 and key < customList[j]:
                    customList[j+1] = customList[j]
                    j -= 1
                customList[j+1] = key
                yield customList

        def visulize_insertion_sort(customList):
            fig, ax = plt.subplots()
            bar_rects = ax.bar(range(len(customList)), customList, align="edge")
            ax.set_xlim(0, len(customList))
            ax.set_ylim(0, 1.1*max(customList))

            def update_bars(array, rects):
                for rect, val in zip(rects, array):
                    rect.set_height(val)
            
            generator = insertion_sort(customList)
            
            def animate(frame):
                array = next(generator)
                update_bars(array, bar_rects)
                
            ani = matplotlib.animation.FuncAnimation(fig, animate, frames=range(len(customList)* len(customList)) , repeat=False, interval=200)
            plt.show()

        random_array = random.sample(range(1,100), 20)
        visulize_insertion_sort(random_array)    
    
    def bucket_sort(self):
        def insertionSort(customList):
            for i in range(1, len(customList)):
                key = customList[i]
                j = i - 1
                while j >= 0 and key < customList[j]:
                    customList[j+1] = customList[j]
                    j -= 1
                customList[j+1] = key
            return customList

        def bucketSort(customList):
            numberofBuckets = round(math.sqrt(len(customList)))
            maxValue = max(customList)
            arr = []
            
            for i in range(numberofBuckets):
                arr.append([])
                
            for j in customList:
                index_b = math.ceil(j*numberofBuckets/maxValue)
                arr[index_b - 1].append(j)
            
            for i in range(numberofBuckets):
                arr[i] = insertionSort(arr[i])
            
            k =  0
            
            for i in range(numberofBuckets):
                for j in range(len(arr[i])):
                    customList[k] = arr[i][j]
                    k += 1
                    yield customList  

        def visualize_bucket_sort(customList):
            fig, ax = plt.subplots()
            bar_rects = ax.bar(range(len(customList)), customList, align="edge")

            def update_bars(array, rects):
                for rect, val in zip(rects, array):
                    rect.set_height(val)

            generator = bucketSort(customList.copy()) 
            
            def animate(frame):
                array = next(generator, None)
                if array is not None:
                    update_bars(array, bar_rects)
            
            ani = matplotlib.animation.FuncAnimation(fig, animate, frames=range(len(customList)*len(customList)), repeat=False, interval=200)
            plt.show()

        random_array = random.sample(range(1,100), 20)
        visualize_bucket_sort(random_array)
    
    def merge_sort(self):
        def merge(customList, l, m, r, frames):
            n1 = m - l + 1
            n2 = r - m

            L = [0] * n1
            R = [0] * n2

            for i in range(n1):
                L[i] = customList[l + i]

            for j in range(n2):
                R[j] = customList[m + 1 + j]

            i = 0
            j = 0
            k = l

            while i < n1 and j < n2:
                if L[i] <= R[j]:
                    customList[k] = L[i]
                    i += 1
                else:
                    customList[k] = R[j]
                    j += 1
                k += 1
                frames.append(customList.copy())

            while i < n1:
                customList[k] = L[i]
                i += 1
                k += 1
                frames.append(customList.copy())

            while j < n2:
                customList[k] = R[j]
                j += 1
                k += 1
                frames.append(customList.copy())

        def mergeSort(customList, l, r, frames):
            if l < r:
                m = (l + (r - 1)) // 2
                mergeSort(customList, l, m, frames)
                mergeSort(customList, m + 1, r, frames)
                merge(customList, l, m, r, frames)

        def animate_merge_sort(customList):
            frames = [customList.copy()]
            mergeSort(customList, 0, len(customList) - 1, frames)

            fig, ax = plt.subplots()
            bar_rects = ax.bar(range(len(customList)), customList, align="center")

            def update(frame):
                for rect, val in zip(bar_rects, frame):
                    rect.set_height(val)

            ani = matplotlib.animation.FuncAnimation(fig, update, frames=frames, repeat=False, blit=False, interval=200)
            plt.show()

        
        customList = random.sample(range(0,100),20)
        animate_merge_sort(customList)

    def quick_sort(self):
        
        def swap(my_list, index1, index2):
            my_list[index1], my_list[index2] = my_list[index2], my_list[index1]

        
        def pivot(my_list, pivot_index, end_index, snapshots):
            swap_index = pivot_index
            for i in range(pivot_index + 1, end_index + 1):
                if my_list[i] < my_list[pivot_index]:
                    swap_index += 1
                    swap(my_list, swap_index, i)
                    snapshots.append(my_list[:])
            swap(my_list, pivot_index, swap_index)
            snapshots.append(my_list[:])
            return swap_index

        
        def quickSort_helper(my_list, left, right, snapshots):
            if left < right:
                pivot_index = pivot(my_list, left, right, snapshots)
                quickSort_helper(my_list, left, pivot_index - 1, snapshots)
                quickSort_helper(my_list, pivot_index + 1, right, snapshots)
            return my_list

       
        def quickSort_visualize(my_list):
            snapshots = [my_list[:]]
            quickSort_helper(my_list, 0, len(my_list) - 1, snapshots)
            return snapshots

        
        def animate_quickSort(snapshots):
            fig, ax = plt.subplots()
            bar_rects = ax.bar(range(len(snapshots[0])), snapshots[0], align="edge")
            ax.set_xlim(0, len(snapshots[0]))
            ax.set_ylim(0, int(1.1 * max(snapshots[0])))

            iteration = [0]

            def update_plot(frame):
                for rect, val in zip(bar_rects, snapshots[frame]):
                    rect.set_height(val)
                iteration[0] += 1
                return bar_rects

            anim = animation.FuncAnimation(fig, update_plot, frames=range(len(snapshots)), repeat=False, blit=False)
            plt.show()

        
        test_list = random.sample(range(0,100),20)
        snapshots = quickSort_visualize(test_list)
        animate_quickSort(snapshots)

    
root = Tk()
root.title("Sorting Algorithms")
mb = MyButton(root)

root.mainloop()
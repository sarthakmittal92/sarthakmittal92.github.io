#include <iostream>
#include <bits/stdc++.h>
#include <time.h>
#include <fstream>
#include <string>
#include <cmath>
using namespace std;

long long int comparisons = 0;
long long int swaps = 0;

const int arrayMin = 0;
const int arrayMax = 100;

void swapper(double A[], int i, int j)
{
    swaps++;
    double temp = A[i];
    A[i] = A[j];
    A[j] = temp;
}

int PP1(double A[], int p, int r)
{
    int x = A[0], i = p - 1;
    for (int j = p; j < r; j++)
    {
        if (A[j] < x)
        {
            comparisons++;
            i++;
            swapper(A, i, j);
        }
    }
    swapper(A, i + 1, r);
    return i + 1;
}

void QSP1(double A[], int p, int r)
{
    if (p < r)
    {
        int q = PP1(A, p, r);
        QSP1(A, p, q - 1);
        QSP1(A, q + 1, r);
    }
}

int PPR(double A[], int p, int r)
{
    int pivot = (p - 1) + (rand() % (r + 1 - p));
    int x = A[pivot], i = p - 1;
    for (int j = p; j < r; j++)
    {
        if (A[j] < x)
        {
            comparisons++;
            i++;
            swapper(A, i, j);
        }
    }
    swapper(A, i + 1, r);
    return i + 1;
}

void QSRP(double A[], int p, int r)
{
    if (p < r)
    {
        int q = PPR(A, p, r);
        QSRP(A, p, q - 1);
        QSRP(A, q + 1, r);
    }
}

void BuSo(double A[], int n)
{
    for (int i = 0; i < n - 1; i++)
    {
        for (int j = 0; j < n - i - 1; j++)
        {
            if (A[j] > A[j + 1])
            {
                comparisons++;
                swapper(A, j, j + 1);
            }
        }
    }
}

double *randArray(const int n)
{
    double *A = new double[n];
    srand(time(0));
    for (int i = 0; i < n; i++)
    {
        A[i] = arrayMin + (double)(rand()) / ((double)(RAND_MAX / (arrayMax - arrayMin)));
    }
    return A;
}

double *almostSorted(const int n)
{
    double *A = randArray(n);
    sort(A, A + n);
    double swapCount = ceil(n / 20);
    for (int i = 0; i < swapCount; i++)
    {
        int index = rand() % (n - 1);
        swapper(A, i, i + 1);
    }
    swaps = 0;
    return A;
}

double *almostSortedReverse(const int n)
{
    double *A = randArray(n);
    sort(A, A + n, greater<double>());
    double swapCount = ceil(n / 20);
    for (int i = 0; i < swapCount; i++)
    {
        int index = rand() % (n - 1);
        swapper(A, i, i + 1);
    }
    swaps = 0;
    return A;
}

int main()
{
    srand(0);
    for (int file = 0; file < 27; file++)
    {
        cout << file << endl;
        string fileNo = to_string(file).c_str();
        ofstream outdata;
        outdata.open("files/data" + fileNo + ".txt"); // data stored in this file
        for (int elements = 1; elements < 1000; elements++)
        {
            outdata << elements << endl; // record elements inserted
            double *A;
            if (file < 9)
            {
                A = randArray(elements);
            }
            else if (file < 18)
            {
                A = almostSorted(elements);
            }
            else
            {
                A = almostSortedReverse(elements);
            }
            if (file % 9 < 3)
            {
                clock_t start = clock(); // timer start
                if (file % 3 == 0)
                {
                    QSP1(A, 0, elements - 1);
                }
                else if (file % 3 == 1)
                {
                    QSRP(A, 0, elements - 1);
                }
                else
                {
                    BuSo(A, elements);
                }
                clock_t end = clock(); // timer ends
                double elapsed = double(end - start);
                outdata << elapsed << endl; // record of time
            }
            else if (file % 9 < 6)
            {
                comparisons = 0;
                if (file % 3 == 0)
                {
                    QSP1(A, 0, elements - 1);
                }
                else if (file % 3 == 1)
                {
                    QSRP(A, 0, elements - 1);
                }
                else
                {
                    BuSo(A, elements);
                }
                outdata << comparisons << endl;
            }
            else
            {
                swaps = 0;
                if (file % 3 == 0)
                {
                    QSP1(A, 0, elements - 1);
                }
                else if (file % 3 == 1)
                {
                    QSRP(A, 0, elements - 1);
                }
                else
                {
                    BuSo(A, elements);
                }
                outdata << swaps << endl;
            }
        }
    }
}
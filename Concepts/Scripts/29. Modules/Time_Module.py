print(help("time"))

"""
O/p: Help on built-in module time:
     
     NAME
         time - This module provides various functions to manipulate time values.
     
     DESCRIPTION
         There are two standard representations of time.  One is the number
         of seconds since the Epoch, in UTC (a.k.a. GMT).  It may be an integer
         or a floating point number (to represent fractions of seconds).
         The epoch is the point where the time starts, the return value of time.gmtime(0).
         It is January 1, 1970, 00:00:00 (UTC) on all platforms.
     
         The other representation is a tuple of 9 integers giving local time.
         The tuple items are:
           year (including century, e.g. 1998)
           month (1-12)
           day (1-31)
           hours (0-23)
           minutes (0-59)
           seconds (0-59)
           weekday (0-6, Monday is 0)
           Julian day (day in the year, 1-366)
           DST (Daylight Savings Time) flag (-1, 0 or 1)
         If the DST flag is 0, the time is given in the regular time zone;
         if it is 1, the time is given in the DST time zone;
         if it is -1, mktime() should guess based on the date and time.
     
     CLASSES
         builtins.tuple(builtins.object)
             struct_time
     
         class struct_time(builtins.tuple)
          |  struct_time(iterable=(), /)
          |
          |  The time value as returned by gmtime(), localtime(), and strptime(), and
          |  accepted by asctime(), mktime() and strftime().  May be considered as a
          |  sequence of 9 integers.
          |
          |  Note that several fields' values are not the same as those defined by
          |  the C language standard for struct tm.  For example, the value of the
          |  field tm_year is the actual year, not year - 1900.  See individual
          |  fields' descriptions for details.
          |
          |  Method resolution order:
          |      struct_time
          |      builtins.tuple
          |      builtins.object
          |
          |  Methods defined here:
          |
          |  __reduce__(...)
          |      Helper for pickle.
          |
          |  __repr__(self, /)
          |      Return repr(self).
          |
          |  ----------------------------------------------------------------------
          |  Static methods defined here:
          |
          |  __new__(*args, **kwargs)
          |      Create and return a new object.  See help(type) for accurate signature.
          |
          |  ----------------------------------------------------------------------
          |  Data descriptors defined here:
          |
          |  tm_gmtoff
          |      offset from UTC in seconds
          |
          |  tm_hour
          |      hours, range [0, 23]
          |
          |  tm_isdst
          |      1 if summer time is in effect, 0 if not, and -1 if unknown
          |
          |  tm_mday
          |      day of month, range [1, 31]
          |
          |  tm_min
          |      minutes, range [0, 59]
          |
          |  tm_mon
          |      month of year, range [1, 12]
          |
          |  tm_sec
          |      seconds, range [0, 61])
          |
          |  tm_wday
          |      day of week, range [0, 6], Monday is 0
          |
          |  tm_yday
          |      day of year, range [1, 366]
          |
          |  tm_year
          |      year, for example, 1993
          |
          |  tm_zone
          |      abbreviation of timezone name
          |
          |  ----------------------------------------------------------------------
          |  Data and other attributes defined here:
          |
          |  __match_args__ = ('tm_year', 'tm_mon', 'tm_mday', 'tm_hour', 'tm_min',...
          |
          |  n_fields = 11
          |
          |  n_sequence_fields = 9
          |
          |  n_unnamed_fields = 0
          |
          |  ----------------------------------------------------------------------
          |  Methods inherited from builtins.tuple:
          |
          |  __add__(self, value, /)
          |      Return self+value.
          |
          |  __contains__(self, key, /)
          |      Return bool(key in self).
          |
          |  __eq__(self, value, /)
          |      Return self==value.
          |
          |  __ge__(self, value, /)
          |      Return self>=value.
          |
          |  __getattribute__(self, name, /)
          |      Return getattr(self, name).
          |
          |  __getitem__(self, key, /)
          |      Return self[key].
          |
          |  __getnewargs__(self, /)
          |
          |  __gt__(self, value, /)
          |      Return self>value.
          |
          |  __hash__(self, /)
          |      Return hash(self).
          |
          |  __iter__(self, /)
          |      Implement iter(self).
          |
          |  __le__(self, value, /)
          |      Return self<=value.
          |
          |  __len__(self, /)
          |      Return len(self).
          |
          |  __lt__(self, value, /)
          |      Return self<value.
          |
          |  __mul__(self, value, /)
          |      Return self*value.
          |
          |  __ne__(self, value, /)
          |      Return self!=value.
          |
          |  __rmul__(self, value, /)
          |      Return value*self.
          |
          |  count(self, value, /)
          |      Return number of occurrences of value.
          |
          |  index(self, value, start=0, stop=9223372036854775807, /)
          |      Return first index of value.
          |
          |      Raises ValueError if the value is not present.
          |
          |  ----------------------------------------------------------------------
          |  Class methods inherited from builtins.tuple:
          |
          |  __class_getitem__(...)
          |      See PEP 585
     
     FUNCTIONS
         asctime(...)
             asctime([tuple]) -> string
     
             Convert a time tuple to a string, e.g. 'Sat Jun 06 16:26:11 1998'.
             When the time tuple is not present, current time as returned by localtime()
             is used.
     
         ctime(...)
             ctime(seconds) -> string
     
             Convert a time in seconds since the Epoch to a string in local time.
             This is equivalent to asctime(localtime(seconds)). When the time tuple is
             not present, current time as returned by localtime() is used.
     
         get_clock_info(...)
             get_clock_info(name: str) -> dict
     
             Get information of the specified clock.
     
         gmtime(...)
             gmtime([seconds]) -> (tm_year, tm_mon, tm_mday, tm_hour, tm_min,
                                    tm_sec, tm_wday, tm_yday, tm_isdst)
     
             Convert seconds since the Epoch to a time tuple expressing UTC (a.k.a.
             GMT).  When 'seconds' is not passed in, convert the current time instead.
     
             If the platform supports the tm_gmtoff and tm_zone, they are available as
             attributes only.
     
         localtime(...)
             localtime([seconds]) -> (tm_year,tm_mon,tm_mday,tm_hour,tm_min,
                                       tm_sec,tm_wday,tm_yday,tm_isdst)
     
             Convert seconds since the Epoch to a time tuple expressing local time.
             When 'seconds' is not passed in, convert the current time instead.
     
         mktime(...)
             mktime(tuple) -> floating point number
     
             Convert a time tuple in local time to seconds since the Epoch.
             Note that mktime(gmtime(0)) will not generally return zero for most
             time zones; instead the returned value will either be equal to that
             of the timezone or altzone attributes on the time module.
     
         monotonic(...)
             monotonic() -> float
     
             Monotonic clock, cannot go backward.
     
         monotonic_ns(...)
             monotonic_ns() -> int
     
             Monotonic clock, cannot go backward, as nanoseconds.
     
         perf_counter(...)
             perf_counter() -> float
     
             Performance counter for benchmarking.
     
         perf_counter_ns(...)
             perf_counter_ns() -> int
     
             Performance counter for benchmarking as nanoseconds.
     
         process_time(...)
             process_time() -> float
     
             Process time for profiling: sum of the kernel and user-space CPU time.
     
         process_time_ns(...)
             process_time() -> int
     
             Process time for profiling as nanoseconds:
             sum of the kernel and user-space CPU time.
     
         sleep(...)
             sleep(seconds)
     
             Delay execution for a given number of seconds.  The argument may be
             a floating point number for subsecond precision.
     
         strftime(...)
             strftime(format[, tuple]) -> string
     
             Convert a time tuple to a string according to a format specification.
             See the library reference manual for formatting codes. When the time tuple
             is not present, current time as returned by localtime() is used.
     
             Commonly used format codes:
     
             %Y  Year with century as a decimal number.
             %m  Month as a decimal number [01,12].
             %d  Day of the month as a decimal number [01,31].
             %H  Hour (24-hour clock) as a decimal number [00,23].
             %M  Minute as a decimal number [00,59].
             %S  Second as a decimal number [00,61].
             %z  Time zone offset from UTC.
             %a  Locale's abbreviated weekday name.
             %A  Locale's full weekday name.
             %b  Locale's abbreviated month name.
             %B  Locale's full month name.
             %c  Locale's appropriate date and time representation.
             %I  Hour (12-hour clock) as a decimal number [01,12].
             %p  Locale's equivalent of either AM or PM.
     
             Other codes may be available on your platform.  See documentation for
             the C library strftime function.
     
         strptime(...)
             strptime(string, format) -> struct_time
     
             Parse a string to a time tuple according to a format specification.
             See the library reference manual for formatting codes (same as
             strftime()).
     
             Commonly used format codes:
     
             %Y  Year with century as a decimal number.
             %m  Month as a decimal number [01,12].
             %d  Day of the month as a decimal number [01,31].
             %H  Hour (24-hour clock) as a decimal number [00,23].
             %M  Minute as a decimal number [00,59].
             %S  Second as a decimal number [00,61].
             %z  Time zone offset from UTC.
             %a  Locale's abbreviated weekday name.
             %A  Locale's full weekday name.
             %b  Locale's abbreviated month name.
             %B  Locale's full month name.
             %c  Locale's appropriate date and time representation.
             %I  Hour (12-hour clock) as a decimal number [01,12].
             %p  Locale's equivalent of either AM or PM.
     
             Other codes may be available on your platform.  See documentation for
             the C library strftime function.
     
         thread_time(...)
             thread_time() -> float
     
             Thread time for profiling: sum of the kernel and user-space CPU time.
     
         thread_time_ns(...)
             thread_time() -> int
     
             Thread time for profiling as nanoseconds:
             sum of the kernel and user-space CPU time.
     
         time(...)
             time() -> floating point number
     
             Return the current time in seconds since the Epoch.
             Fractions of a second may be present if the system clock provides them.
     
         time_ns(...)
             time_ns() -> int
     
             Return the current time in nanoseconds since the Epoch.
     
     DATA
         altzone = -23400
         daylight = 0
         timezone = -19800
         tzname = ('India Standard Time', 'India Daylight Time')
     
     FILE
         (built-in)
     
     
     None
"""
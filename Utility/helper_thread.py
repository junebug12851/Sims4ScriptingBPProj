from concurrent.futures import ThreadPoolExecutor, as_completed

def _default_multithread_run_callback(name, result):
    print(f'{name}: {result}')

def multithread_run(fn, callback=_default_multithread_run_callback, args_list=()):
    """run functions concurrently, call callback with (name, result) on every task done.

    """
    with ThreadPoolExecutor(max_workers=5) as executor:
        # Start the load operations and mark each future with its URL
        future_tasks = {executor.submit(fn, *args, **kwargs): name for name, args, kwargs in args_list}
        for future in as_completed(future_tasks):
            name = future_tasks[future]
            try:
                result = future.result()
                callback(name, result)
            except Exception as exc:
                print(f'multithread_run {fn.__name__} {name} failed: \n{exc}')

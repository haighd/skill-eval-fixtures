export interface Database {
  query<T = unknown>(sql: string, params?: unknown[]): Promise<T[]>;
  get<T = unknown>(table: string, id: string): Promise<T | undefined>;
  insert(table: string, row: object): Promise<void>;
  save(table: string, row: object): Promise<void>;
  delete(table: string, id: string): Promise<void>;
}

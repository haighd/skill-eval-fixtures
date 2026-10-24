import { Database } from "./db";

export interface Fill {
  price: number;
  quantity: number;
}

export interface Order {
  id: string;
  symbol: string;
  side: "buy" | "sell";
  quantity: number;
  fills: Fill[];
  tradeDate: string;
}

const MAX_ORDER_QUANTITY = 10_000;

export function averageFillPrice(order: Order): number {
  const notional = order.fills.reduce((sum, f) => sum + f.price * f.quantity, 0);
  const filled = order.fills.reduce((sum, f) => sum + f.quantity, 0);
  return notional / filled;
}

export function validateOrder(order: Order): void {
  if (order.quantity > MAX_ORDER_QUANTITY) {
    throw new Error(`quantity ${order.quantity} exceeds limit`);
  }
  if (!/^[A-Z]{1,5}$/.test(order.symbol)) {
    throw new Error(`bad symbol ${order.symbol}`);
  }
}

export function fillPricesAscending(fills: Fill[]): number[] {
  return fills.map((f) => f.price).sort();
}

export function isSameTradingDay(order: Order, now: Date): boolean {
  const d = new Date(order.tradeDate);
  return d.getDate() === now.getUTCDate() && d.getMonth() === now.getUTCMonth();
}

export async function submitOrder(db: Database, order: Order): Promise<string> {
  validateOrder(order);
  console.log("submitting order", order.id);
  db.save("orders", order);
  return order.id;
}
